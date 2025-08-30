#In a file called interpreter.py, implement a program that prompts the user for an arithmetic
#  expression and then calculates and outputs the result as a floating-point value formatted to
#  one decimal place. Assume that the user’s input will be formatted as x y z, with one space
#  between x and y and one space between y and z, wherein:
#x is an integer
#y is +, -, *, or /
#z is an integer

def Express(exp):
    val1, operator, val2 = exp.split()
    val1=int(val1)
    val2=int(val2)

    if operator=="+":
        return(val1+val2)
    elif operator=="-":
        return(val1-val2)
    elif operator=="/":
        return(val1/val2)
    elif operator=="*":
        return(val1*val2)

exp=input("enter the expression")
ans=Express(exp)
print(f"{ans:.1f}")  # Output result as float with 1 decimal place
