#In plates.py, implement a program that prompts the user for a vanity plate and then output
#  Valid if meets all of the requirements or Invalid if it does not. Assume that any letters
#  in the user’s input will be uppercase. Structure your program per the below, wherein is_valid 
# returns True if s meets all requirements and False if it does not. Assume that s will be a str.
#  You’re welcome to implement additional functions for is_valid to call (e.g., one function per 
# requirement).


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 2: length check
    if not (2 <= len(s) <= 6):
        return False

    # Rule 1: first two must be letters
    if not s[0:2].isalpha():
        return False

    # Rule 5: must be alphanumeric only
    if not s.isalnum():
        return False

    # Rule 3 and 4: number placement rules
    for i, ch in enumerate(s):
        if ch.isdigit():
            # Rule 4: first number can't be 0
            if ch == "0":
                return False
            # After the first digit, everything must be digits
            if not s[i:].isdigit():
                return False
            return True #return True if all above conditions are true

    return True #if plate has no digits at all
main()
