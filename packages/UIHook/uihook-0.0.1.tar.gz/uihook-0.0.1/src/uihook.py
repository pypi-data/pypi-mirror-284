import os
import asyncio
import time
import random
import string
import logging
from typing import Dict, Any, Optional, List
from functools import wraps
from multiprocessing import Process, Event, Value, Queue

import requests
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import tkinter as tk
import customtkinter as ctk
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global variables
app_instance: Optional[Any] = None
app_process: Optional[Process] = None
app_ready = Event()
app_running = Value('b', False)
app_fully_initialized = Value('b', False)
command_queue = Queue()
result_queue = Queue()

app = FastAPI()

# API Key authentication
API_KEY = os.getenv("UIHOOK_API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key")

def api_key_auth(api_key: str = Depends(api_key_header)):
    if API_KEY and api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API Key")
    return api_key

# Decorator to wrap Tkinter/CustomTkinter classes
def uihook(cls):
    if not issubclass(cls, (tk.Widget, ctk.CTk)):
        raise TypeError(f"{cls.__name__} is not a Tkinter or CustomTkinter class")

    @wraps(cls)
    def wrapper(*args, **kwargs):
        global app_instance
        instance = cls(*args, **kwargs)
        app_instance = instance
        logger.info(f"Created instance of {cls.__name__}")
        app_ready.set()
        app_running.value = True
        app_fully_initialized.value = True
        logger.info("Application fully initialized")
        return instance

    return wrapper

class Command(BaseModel):
    method: str
    args: List[Any] = []

@app.post("/interact", dependencies=[Depends(api_key_auth)])
async def interact(command: Command):
    logger.info(f"Received interact command: {command}")
    if not app_running.value:
        logger.warning("No application instance found")
        return {"status": "Error", "message": "No application instance found"}

    command_queue.put((command.method, command.args))
    try:
        result = result_queue.get(timeout=10)
        logger.info(f"Successfully executed {command.method}")
        return {"status": "Success", "result": result}
    except Exception as e:
        logger.error(f"Error executing {command.method}: {str(e)}")
        return {"status": "Error", "message": str(e)}

@app.post("/shutdown", dependencies=[Depends(api_key_auth)])
async def shutdown():
    logger.info("Received shutdown command")
    global app_process
    if app_running.value:
        command_queue.put(("quit", []))
        try:
            result_queue.get(timeout=10)
        except:
            pass
        app_running.value = False
        app_fully_initialized.value = False
    if app_process:
        app_process.terminate()
        app_process.join(timeout=10)
        if app_process.is_alive():
            logger.warning("Application process did not terminate, forcing...")
            app_process.kill()
            app_process.join()
        app_process = None
        logger.info("Application process terminated")
    app_ready.clear()
    return {"status": "Application shut down"}

@app.post("/startup", dependencies=[Depends(api_key_auth)])
async def startup():
    logger.info("Received startup command")
    global app_process
    if not app_running.value:
        app_ready.clear()
        app_fully_initialized.value = False
        app_process = Process(target=start_app)
        app_process.start()
        logger.info("Started application process")
        
        start_time = time.time()
        while not app_ready.is_set():
            if time.time() - start_time > 30:
                logger.error("Timeout waiting for application to start")
                return {"status": "Error", "message": "Application failed to start in time"}
            await asyncio.sleep(0.1)
        
        logger.info("Application process started successfully")
        return {"status": "Application started"}
    else:
        logger.warning("Application is already running")
        return {"status": "Application already running"}

@app.get("/status", dependencies=[Depends(api_key_auth)])
async def status():
    logger.info("Received status request")
    status_info = {
        "application_running": app_running.value,
        "application_fully_initialized": app_fully_initialized.value
    }
    logger.info(f"Current status: {status_info}")
    return status_info

@app.get("/wait_for_initialization", dependencies=[Depends(api_key_auth)])
async def wait_for_initialization():
    logger.info("Waiting for application to fully initialize")
    start_time = time.time()
    while not app_fully_initialized.value:
        if time.time() - start_time > 30:
            logger.error("Timeout waiting for application to initialize")
            return {"status": "Error", "message": "Timeout waiting for application to initialize"}
        await asyncio.sleep(0.1)
    logger.info("Application fully initialized")
    return {"status": "Success", "message": "Application fully initialized"}

def start_app():
    global app_instance
    app_module = os.getenv("UIHOOK_APP_MODULE")
    app_class = os.getenv("UIHOOK_APP_CLASS")

    if not app_module or not app_class:
        raise ValueError("UIHOOK_APP_MODULE and UIHOOK_APP_CLASS must be set in environment variables")

    module = __import__(app_module, fromlist=[app_class])
    app_cls = getattr(module, app_class)
    app = app_cls()
    app_instance = app
    logger.info(f"Started {app_class} instance")
    
    def check_queue():
        try:
            method, args = command_queue.get_nowait()
            if method == "quit":
                app.quit()
                result_queue.put(None)
            else:
                result = getattr(app, method)(*args)
                result_queue.put(result)
        except:
            pass
        app.after(100, check_queue)
    
    check_queue()
    app.mainloop()

def generate_api_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=64))

def run_server(host: str, port: int, api_key: Optional[str]):
    global API_KEY
    if api_key == "":
        API_KEY = generate_api_key()
        logger.info(f"Generated API Key: {API_KEY}")
    elif api_key:
        API_KEY = api_key

    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    config = Config()
    config.bind = [f"{host}:{port}"]
    asyncio.run(serve(app, config))
