'''In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the 
below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is a positive integer, 
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
 If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
  If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.'''

def main():
    fraction = input("Fraction: ")
    try:
        percent = convert(fraction)
        print(gauge(percent))
    except (ValueError, ZeroDivisionError):
        pass   # ignore invalid input, as per problem spec


def convert(fraction: str) -> int:
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("X and Y must be integers")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    if x > y:
        raise ValueError("X cannot be greater than Y")

    return round((x / y) * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()