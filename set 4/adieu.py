'''In a file called adieu.py, implement a program that prompts the user for names, one per line,
 until the user inputs control-d. Assume that the user will input at least one name. Then bid 
 adieu to those names, separating two names with one and, three names with two commas and one 
 and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:'''



import inflect
p=inflect.engine()
names=[]    #Create List and not tuple, values will not be able to append
while True:
    try:
        name=input("Name: ")
        names.append(name)
    except EOFError:
        break
print(f"Adieu, adieu, to {p.join(tuple(names))}")       #Creating Tuple later on 