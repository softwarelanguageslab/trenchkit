import importlib
import os
import sys
import argparse

TOOLS_DIR = os.path.join(os.path.dirname(__file__), "tools")

def load_tools():
    tools = {}
    dirs = filter(lambda d: os.path.isdir(os.path.join(TOOLS_DIR, d)), os.listdir(TOOLS_DIR))
    dirs = filter(lambda d: not d.startswith("__"), dirs)
    for dirname in dirs:
        module = importlib.import_module(f"trenchkit.tools.{dirname}.main")
        tools[dirname] = module.run
    return tools

def main():
    tools = load_tools()

    parser = argparse.ArgumentParser(description="Tools Program")
    parser.add_argument("tool", choices=tools.keys(), help="The tool to run")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments for the tool")
    args, unknown = parser.parse_known_args()

    if args.tool in tools:
        print(f"Running tool: {args.tool}")
        tools[args.tool](args.args)
    else:
        print(f"Tool '{args.tool}' not found.")

if __name__ == "__main__":
    main()