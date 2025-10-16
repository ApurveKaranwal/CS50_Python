'''In a file called response.py, using either validator-collection or validators from PyPI, implement 
a program that prompts the user for an email address via input and then prints Valid or Invalid, 
respectively, if the input is a syntatically valid email address. You may not use re. And do not 
validate whether the email address’s domain name actually exists.'''

import validators

def main():
    email = input("What's your email address? ").strip()
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()