'''In a file called grocery.py, implement a program that prompts the user for items, one per line,
 until the user inputs control-d (which is a common way of ending one’s input to a program). 
 Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing 
 each line with the number of times the user inputted that item. No need to pluralize the items. 
 Treat the user’s input case-insensitively.'''

items=[]
single_item={}

while True:
    try:
        item=input("ITEM: ").strip().lower()
        items.append(item)

    except EOFError:
        break
    
for i in items:
    count=0
    for j in items:
        if i==j:
            count+=1
    if i not in single_item:
        single_item[i]=count

for name, count in sorted(single_item.items()):
    print(count, name.upper())
    