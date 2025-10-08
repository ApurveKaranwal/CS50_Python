'''In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as 
input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other 
functions as you see fit, but you may not import any other libraries. You’re welcome, but not required,
to use re and/or sys.

#.#.#.# ...But each # should be a number between 0 and 255'''


import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression for a valid IPv4 address
    pattern = re.compile(
        r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    )
    match = pattern.match(ip)
    if not match:
        return False
    
    # Check that each group is between 0 and 255
    for part in match.groups():
        if int(part) < 0 or int(part) > 255:
            return False
    return True


if __name__ == "__main__":
    sys.exit(main())