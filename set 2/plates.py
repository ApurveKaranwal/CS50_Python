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
            break

    return True


main()
