#In a file called pizza.py, implement a program that expects exactly one 
# command-line argument, the name (or path) of a CSV file in Pinocchio’s 
# format, and outputs a table formatted as ASCII art using tabulate, 
# a package on PyPI at pypi.org/project/tabulate. Format the table using 
# the library’s grid format. If the user does not specify exactly one
#  command-line argument, or if the specified file’s name does not end 
# in .csv, or if the specified file does not exist, the program should 
# instead exit via sys.exit.

from tabulate import tabulate
import sys
import csv


def main():
    if len(sys.argv)!=2:
        sys.exit("Usage: python pizza.py filename.csv")
    filename=sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename,'r') as file:
            reader=csv.DictReader(file)
            table = [row.values() for row in reader]
            headers = reader.fieldnames
            print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
    
    



