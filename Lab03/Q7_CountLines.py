import sys
from pathlib import Path

args = sys.argv
args.pop(0)
for arg in args:
    file_path = Path(__file__).parent.joinpath(arg)
    try:
        f = open(file_path, "r")
        print(f"Filename: {arg}. Number of lines: {str(len(f.readlines()))}")
    except FileNotFoundError:
        print(f"{arg} is not found!")
