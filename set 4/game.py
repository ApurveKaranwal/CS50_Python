'''In a file called game.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.'''

from random import randint

level=int(input("Level: "))
while True:
    try:
        if level>=1:
            break
    except ValueError:
        continue

rndInt=randint(1,level)

while True:
    try:
        guess=int(input("Guess: "))
        if guess<=0:
            continue
    except ValueError:
        continue

    if guess < rndInt:
        print("Too small!")
    elif guess > rndInt:
        print("Too large!")
    else:
        print("Just right!")
        break





    


