'''In a file called professor.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits.
 No need to support operations other than addition (+).'''



import random


def main():
    level=get_level()
    score=0

    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        correct=x+y
        
        tries=0
        while tries<3:
            try:
                answer=int(input(f"{x}+{y} = "))
                if answer ==correct:
                    score+=1
                    break
                else:
                    print("EEE")
                    tries+=1
            except ValueError:
                tries+=1
        if tries==3:
            print(f"{x}+{y}={correct}")
        print("Score: ",score)


def get_level():
    while True:
        try:
            level= int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass
            

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:  # level == 3
        return random.randint(100, 999)


if __name__ == "__main__":
    main()