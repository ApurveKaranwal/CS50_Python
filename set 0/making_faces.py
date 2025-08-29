#In a file called faces.py, implement a function called convert that accepts a str as input 
# and returns that same input with any :) converted to 🙂 
# (otherwise known as a slightly smiling face) and any :( converted to 🙁 
# (otherwise known as a slightly frowning face). All other text should be returned unchanged.

def convert(string1):
    print("original string is",string1)
    if ':)' in string1:
        string1 = string1.replace(':)', '🙂')
        print(string1)
    if ':(' in string1:
        string1 = string1.replace(':(', '🙁')
        print(string1)
strr=input("enter a string :")
convert(strr)