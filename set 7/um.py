'''In a file called um.py, implement a function called count that expects a line of text as input as a 
str and returns, as an int, the number of times that “um” appears in that text, case-insensitively, as
 a word unto itself, not as a substring of some other word. For instance, given text like hello, um, 
 world, the function should return 1. Given text like yummy, though, the function should return 0.

Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as
 you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re 
 and/or sys.'''

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # \b ensures "um" is a word by itself (word boundaries)
    # re.IGNORECASE makes it case-insensitive
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
