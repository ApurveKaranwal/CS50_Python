#In a file called fuel.py, implement a program that prompts the user for a fraction,
#  formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, 
# as a percentage rounded to the nearest integer, how much fuel is in the tank.
#  If, though, 1% or less remains, output E instead to indicate that the tank is 
# essentially empty. And if 99% or more remains, output F instead to indicate that the 
# tank is essentially full.

def main(x,y):
    try:
        if x/y>1:     #invalid case where % will be more than 100
            return False   
        fuel=calcFuel(x,y)
        if fuel<=1:
            print("E")
        elif fuel>=99:
            print("F")
        else:
            print(f"{fuel}%")
        return True
    except (ValueError, ZeroDivisionError):
        return None



def calcFuel(x,y):
    frac=x/y
    perc=frac*100
    rndperc=round(perc)
    return rndperc
while True:
    fract=input("Fraction: ")
    try:
        x, y=fract.split("/")
        x=int(x)
        y=int(y)
        
        if y==0:    #To prevent ZeroDivisionError
            continue
        if main(x,y): #If main() works, while loop breaks
            break

    except (ValueError, ZeroDivisionError):
        continue

