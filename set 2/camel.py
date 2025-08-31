'''In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.'''

def main(str1):
    snake_case = ""
    for i in str1:
        if i.isupper():
            snake_case += "_"+ i.lower()
        else:
            snake_case += i
    print(snake_case)   #move it outside of loop

str1=input("enter a variable name in camelCase :")
main(str1)