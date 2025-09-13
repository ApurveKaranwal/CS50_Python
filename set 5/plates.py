'''In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code
 per the below, wherein is_valid still expects a str as input and returns True if that str meets all
  requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

  “All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 
characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, 
AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number 
used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”'''


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2<=len(s)<=6: #length of plate should be more than 2
        return False
    
    if not s[0:2].isalpha():  #starting 2 letter should be from alphabet, not digit
        return False
    
    if not s.isalnum():         #if Plate contains any special symbol
        return False

    for i, ch in enumerate(s):
        if ch.isdigit():
            # if it's the first digit and it's 0 → invalid
            if not s[i-1].isdigit() and ch == "0":
                return False

            # once numbers start, everything after must be digits
            if not s[i:].isdigit():
                return False

    return True


        

if __name__ == "__main__":
    main()