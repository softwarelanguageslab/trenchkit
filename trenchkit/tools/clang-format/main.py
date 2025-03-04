import os
import subprocess
import argparse


def run(args):
	parser = argparse.ArgumentParser(description="clang-format Program")
	parser.add_argument("-t", "--target", help="Path config file", default=".")
	parser.add_argument("-c", "--clang", default="clang-format", help="Clang-Format command")
	parser.add_argument("-s", "--source", help="Config format file")
	parser.add_argument("-i", "--ignore", help="Config ignore file")
	parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
	parsed_args, unknown = parser.parse_known_args()

	find_cmd = ["find", parsed_args.target, "-type", "f", "(", "-name", "*.h", "-o", "-name", "*.cpp", "-o", "-name", "*.c", "-o", "-name", "*.hpp", ")"]
    
	if parsed_args.ignore and os.path.exists(parsed_args.ignore):
		with open(parsed_args.ignore, "r") as f:
			for pattern in f:
				pattern = pattern.strip()
				if not pattern or pattern.startswith("#"):
					continue
				find_cmd.extend(["!", "-path", pattern])
    
	verbose_flag = ["-verbose"] if parsed_args.verbose else []
	cfile_source = [f"-style=file:{parsed_args.source}"] if parsed_args.source else []
	find_cmd.extend(["-exec", parsed_args.clang, "-i", *verbose_flag, *cfile_source, "{}", "+"])

    
	print("Running:", " ".join(find_cmd))
    
	subprocess.run(find_cmd, check=True)
    
	print("Formatting complete.")