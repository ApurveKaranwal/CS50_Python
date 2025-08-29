#In a file called einstein.py, implement a program in Python that prompts 
# the user for mass as an integer (in kilograms) and then outputs the equivalent 
# number of Joules as an integer.
#  Assume that the user will input an integer.

def calcEnergy(mass):
    print(f"formula is  𝐸 =𝑚⁢𝑐2")
    c=300000000
    energy=mass*c*c
    print(f"final answer is {energy}")

mass=int(input("enter mass of object :"))
calcEnergy(mass)
    