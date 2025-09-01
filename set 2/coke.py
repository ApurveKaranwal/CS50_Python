'''In a file called coke.py, implement a program that prompts the user to insert a coin, 
one at a time, each time informing the user of the amount due. Once the user has inputted 
at least 50 cents, output how many cents in change the user is owed. Assume that the user
 will only input integers, and ignore any integer that isn’t an accepted denomination.'''


cost=50
print("Amount Due :",cost)
coinGiven=0
domination=[5,10,25]
while cost>coinGiven:
    coin=int(input("Insert Coin :"))
    if coin in domination:
        coinGiven+=coin
    #else:
#print("only domination of 5, 10, 25 cents is allowed")
    if cost-coinGiven>=0:
        print("Amount Due:",cost-coinGiven)

if coinGiven>cost:
    print("change owed",coinGiven-cost)


