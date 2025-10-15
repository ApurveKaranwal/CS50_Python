'''In a file called working.py, implement a function called convert that expects a str in any of the 12-hour 
formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that 
AM and PM will be capitalized (with no periods therein) and that there will be a space before each. 
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM 
specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either 
time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will 
start ante meridiem and end post meridiem; someone might work late and even long 
hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other 
functions as you see fit, but you may not import any other libraries. You’re welcome, but not
required, to use re and/or sys.'''

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Match valid formats like:
    # 9 AM to 5 PM
    # 9:00 AM to 5 PM
    # 9 AM to 5:00 PM
    # 9:00 AM to 5:00 PM
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    
    if not match:
        raise ValueError("Invalid format")

    # Extract matched groups
    h1, m1, p1, h2, m2, p2 = match.groups()

    # Convert to int and default missing minutes to 00
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    # Validate time range
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12 and 0 <= m1 < 60 and 0 <= m2 < 60):
        raise ValueError("Invalid time values")

    # Convert to 24-hour format
    h1 = to_24_hour(h1, p1)
    h2 = to_24_hour(h2, p2)

    # Return formatted result
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def to_24_hour(hour, period):
    """Convert 12-hour time to 24-hour time."""
    if period == "AM":
        return 0 if hour == 12 else hour
    elif period == "PM":
        return hour if hour == 12 else hour + 12
    else:
        raise ValueError("Invalid period")


if __name__ == "__main__":
    main()
