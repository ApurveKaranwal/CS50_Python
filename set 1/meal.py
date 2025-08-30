#In meal.py, implement a program that prompts the user for a time and outputs 
# whether it’s breakfast time, lunch time, or dinner time. If it’s not time for 
# a meal, don’t output anything at all. Assume that the user’s input will be 
# formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time 
# range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime
# in between, it’s time for breakfast.

def main():
    time=input("enter time :")
    hour=convert(time)

    if 7.0<=hour<=8.0:
        print("breakfast time")
    elif 12.0<=hour<=13.0:
        print("lunch time")
    elif 18.0<=hour<=19.0:
        print("dinner time")
    


def convert(time):
    hour, minute=time.split(":")
    hour=int(hour)
    minute=int(minute)
    return hour + minute / 60
    


#if __name__ == "__main__":
   # main()
main()