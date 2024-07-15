import argparse
import os
import toml
from uihook import run_server

def get_entry_point():
    with open("pyproject.toml", "r") as f:
        pyproject = toml.load(f)

    scripts = pyproject.get("project", {}).get("scripts", {})
    if len(scripts) == 1:
        return list(scripts.values())[0]
    elif len(scripts) > 1:
        raise ValueError("Multiple entry points found. Please specify the entry point using --entry-point.")
    else:
        raise ValueError("No entry points found in pyproject.toml.")

def main():
    parser = argparse.ArgumentParser(description="UIHook Server")
    parser.add_argument("-H", "--host", default="127.0.0.1", help="Host to bind the server to")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Port to bind the server to")
    parser.add_argument("--api-key", nargs="?", const="", help="API key for authentication. If specified without a value, a key will be generated.")
    parser.add_argument("--entry-point", help="Entry point of the application (e.g., 'src.app:main').")
    args = parser.parse_args()

    entry_point = args.entry_point or get_entry_point()
    if not entry_point:
        raise ValueError("No entry point specified or found in pyproject.toml.")

    module, app_class = entry_point.split(":")
    os.environ["UIHOOK_APP_MODULE"] = module
    os.environ["UIHOOK_APP_CLASS"] = app_class

    run_server(args.host, args.port, args.api_key)

if __name__ == "__main__":
    main()
