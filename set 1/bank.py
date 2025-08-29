#In a file called bank.py, implement a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. If the greeting starts 
# with an “h” (but not “hello”), output $20. Otherwise, output $100.
#  Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting 
# case-insensitively

def greeting(greet):
    ngreet=greet.split()
    if ngreet[0].lower()=="hello":
        print("$100")
    elif ngreet[0][0].lower()=="h": #error (ngreet[0][0] == "h") or ("H")
        print("$20")                #fix elif ngreet[0][0] == "h" or ngreet[0][0] == "H":
    else:
        print("$o")

greet=input("enter a greeting :")
greeting(greet)