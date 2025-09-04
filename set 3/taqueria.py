'''In a file called taqueria.py, implement a program that enables a user to place an 
order, prompting them for items, one per line, until the user inputs 
control-d (which is a common way of ending one’s input to a program).
 After each inputted item, display the total cost of all items inputted thus far, prefixed with 
 a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively
 . Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.'''

class food():
    def __init__(self):
        self.foodData={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    def cost(self,Fitem):
        Fitem=Fitem.title().strip()
        if Fitem in self.foodData:
            return (f"{self.foodData[Fitem]}")
        else:
            return None



def main():
    cost=0
    while True:
        try:
            name=input("Item: ")
            price=food().cost(name)
            price=float(price)
            cost+=price
            print(f"Total:${cost:.2f}")
        except EOFError:    #press ctrl+z then press enter, leads to EOFFrror
            print()
            break

if __name__ == "__main__":
    main()