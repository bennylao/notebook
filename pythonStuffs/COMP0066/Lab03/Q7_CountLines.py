import sys
from pathlib import Path

# to run this pythonStuffs script:
# pythonStuffs pythonStuffs.Lab03/Q7_CountLines.py file1.txt file2.txt file3.txt
args = sys.argv
args.pop(0)
for arg in args:
    file_path = Path(__file__).parent.joinpath(arg)
    try:
        f = open(file_path, "r")
        print(f"Filename: {arg}. Number of lines: {str(len(f.readlines()))}")
    except FileNotFoundError:
        print(f"{arg} is not found!")
