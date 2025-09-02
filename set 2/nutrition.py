#In a file called nutrition.py, implement a program that prompts consumers users to input 
# a fruit (case-insensitively) and then outputs the number of Calories in one portion of 
# that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization
#  aside, assume that users will input fruits exactly as written in the poster
#  (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

def Calories(fruit):
    fruit=fruit.lower()
    if fruit=="apple":
        print("Calories:130 ")
    elif fruit=="avocado california":
        print("Calories:50")
    elif fruit=="banana":
        print("Calories:110")
    elif fruit=="cantaloupe":
        print("Calories:50")
    elif fruit=="grapefruit":
        print("Calories:60")
    elif fruit=="grapes":
        print("Calories:90")
    elif fruit=="honeydew melon":
        print("Calories:50")
    elif fruit == "kiwifruit":
        print("Calories: 90")
    elif fruit == "lemon":
        print("Calories: 15")
    elif fruit == "lime":
        print("Calories: 20")
    elif fruit == "nectarine":
        print("Calories: 60")
    elif fruit == "orange":
        print("Calories: 80")
    elif fruit == "peach":
        print("Calories: 60")
    elif fruit == "pear":
        print("Calories: 100")
    elif fruit == "pineapple":
        print("Calories: 50")
    elif fruit == "plums":
        print("Calories: 70")
    elif fruit == "strawberries":
        print("Calories: 50")
    elif fruit == "sweet cherries":
        print("Calories: 100")
    elif fruit == "tangerine":
        print("Calories: 50")
    elif fruit == "watermelon":
        print("Calories: 80")
    else:
        return
        
def main():
    name=input("Item: ").strip()
    Calories(name)

if __name__=="__main__":
    main()
