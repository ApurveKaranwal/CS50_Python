'''
In a file called figlet.py, implement a program that:
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.'''

import sys
from pyfiglet import Figlet
import random

def RandText(s):
    figlet = Figlet()
    lst1=figlet.getFonts()
    rndFont=random.choice(lst1)
    figlet.setFont(font=rndFont)
    return figlet.renderText(s)
        
if len(sys.argv)==1:
    str1=input("Input: ")
    str1=RandText(str1)
    print(f"{str1}")

elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    str1=input("Input: ")
    figlet = Figlet()
    font1=sys.argv[2]
    figlet.setFont(font=font1)
    print(figlet.renderText(str1))

else:
    sys.exit("Invalid usage")




    


