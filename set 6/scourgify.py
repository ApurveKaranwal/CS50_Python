#In a file called scourgify.py, implement a program that:

#Expects the user to provide two command-line arguments:
#the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
#the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
#Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.


import sys
import csv

def main():
    # Check for correct command-line usage
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)
            students = []

            for row in reader:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})

        with open(output_file, "w", newline="") as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()
