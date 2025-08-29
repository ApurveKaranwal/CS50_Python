def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # remove the leading '$' and convert to float
    return float(d.replace("$", "").strip())


def percent_to_float(p):
    # remove the trailing '%' and convert to float (divided by 100 to get decimal)
    return float(p.replace("%", "").strip()) / 100


main()
