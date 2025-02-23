import os
import subprocess
import argparse

CONFIGURATION = {}

def load_configuration():
	with open(os.path.join(os.path.dirname(__file__), "settings.conf"), "r") as configuration_file:
		lines = configuration_file.read().splitlines()
		for line in lines:
			key, value = line.split('=')
			CONFIGURATION[key] = value

def run(args):
	parser = argparse.ArgumentParser(description="clang-format Program")
	parser.add_argument("-path", help="Path for directory to format", default=".")
	parser.add_argument("-cfile", action="store_true", help="Verbose mode")
	parser.add_argument("-v", action="store_true", help="Verbose mode")
	parser.add_argument("args", nargs=argparse.REMAINDER, help="Additional arguments for clang-format")
	parsed_args = parser.parse_args(args)
	
	load_configuration()

	format_file = os.path.join(os.path.dirname(__file__), CONFIGURATION["CLANG_FORMAT_FILE"])
	format_ignore_file = os.path.join(os.path.dirname(__file__), CONFIGURATION["CLANG_IGNORE_FILE"])

	find_cmd = ["find", parsed_args.path, "-type", "f", "(", "-name", "*.h", "-o", "-name", "*.cpp", "-o", "-name", "*.c", "-o", "-name", "*.hpp", ")"]
    
	if os.path.exists(format_ignore_file):
		with open(format_ignore_file, "r") as f:
			for pattern in f:
				pattern = pattern.strip()
				if not pattern or pattern.startswith("#"):
					continue
				find_cmd.extend(["!", "-path", pattern])
    
	verbose_flag = ["-verbose"] if parsed_args.v else []
	cfile_flag = [f"-style=file:{format_file}"] if parsed_args.v else []
	find_cmd.extend(["-exec", CONFIGURATION["CLANG_FORMAT_CALL"], "-i", *verbose_flag, *cfile_flag, "{}", "+"])

    
	print("Running:", " ".join(find_cmd))
    
	subprocess.run(find_cmd, check=True)
    
	print("Formatting complete.")