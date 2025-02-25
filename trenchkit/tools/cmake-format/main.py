import argparse
import os
import subprocess


def format_cmake(target, config):
    if os.path.isdir(target):
        # Find all CMakeLists.txt and .cmake files
        cmake_files = [
            os.path.join(root, file)
            for root, _, files in os.walk(target)
            for file in files
            if file.endswith(("CMakeLists.txt", ".cmake"))
        ]
    else:
        # Single file case
        cmake_files = [target]

    if not cmake_files:
        print(f"No CMake files found in {target}")
        return

    for file in cmake_files:
        command = ["cmake-format", "-i", file]
        if config:
            command.extend(["--config", config])

        try:
            subprocess.run(command, check=True)
            print(f"Formatted: {file}")
        except subprocess.CalledProcessError as e:
            print(f"Error formatting {file}: {e}")

def run(args):
    parser = argparse.ArgumentParser(description="cmake-format Program")
    parser.add_argument("-target", help="Path to the directory or file", default=".")
    parser.add_argument("-config", help="Path to cmake-format config file", default=".cmake-format.yaml")
    parsed_args = parser.parse_args(args)

    format_cmake(parsed_args.target, parsed_args.config)
