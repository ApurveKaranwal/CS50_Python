'''Even so, in a file called lines.py, implement a program that expects exactly 
one command-line argument, the name (or path) of a Python file, and outputs 
the number of lines of code in that file, excluding comments and blank lines. 
If the user does not specify exactly one command-line argument, or if the 
specified file’s name does not end in .py, or if the specified file does not
 exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace,
 is a comment. (A docstring should not be considered a comment.) Assume that 
 any line that only contains whitespace is blank.'''

import sys
import os

def main():
    if len(sys.argv)!=2:
        sys.exit("Usage: python lines.py filename.py")
    
    filename=sys.argv[1]

    if not filename .endswith(".py"):
        sys.exit("Not a python file")

    if not os.path.isfile(filename):
        sys.exit("file do not exists")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            count=0
            for line in file:
                stripped=line.strip()
                if stripped and not stripped.startswith("#"):
                    count += 1
        print(count)
    
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
