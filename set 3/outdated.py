'''In a file called outdated.py, implement a program that prompts the user for a date, anno
 Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the 
 month in the latter might be any of the values in the list below:'''


months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date=input("Date: ")
if "/" in date:
    month, date, year=date.split("/")
    month=int(month)
    date=int(date)
    year=int(year)
    print(f"{year}-{month:02d}-{date:02d}")
elif "," in date:
    month, date, year=date.split(" ")
    date=str(date)
    date = date.replace(",", "")
    date=int(date)
    year=int(year)
    indd=0
    for i in months:
        if i==month:
            ind=int(months.index(i))+1
            indd=ind
    print(f"{year}-{indd:02d}-{date:02d}")
    
    
