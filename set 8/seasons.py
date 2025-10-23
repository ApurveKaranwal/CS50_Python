'''In a file called seasons.py, implement a program that prompts the user for their date of birth in 
YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals, just like the song from Rent, without any and between words.
Since a user might not know the time at which they were born, assume, for simplicity, that the user 
was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the 
same date. Use datetime.date.today to get today’s date, 
per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or 
more other functions as well:'''


import sys
from datetime import date
from num2words import num2words

def main():
    try:
        # Prompt user for birthdate
        birthdate_input = input("Date of Birth: ")
        year, month, day = map(int, birthdate_input.split("-"))
        birthdate = date(year, month, day)
    except ValueError:
        sys.exit("Invalid Date")

    # Get today's date
    today = date.today()

    # Calculate the difference in minutes
    delta = today - birthdate
    minutes = delta.days * 24 * 60

    # Convert minutes to words
    print(num2words(minutes, to='ordinal'))

if __name__ == "__main__":
    main()
