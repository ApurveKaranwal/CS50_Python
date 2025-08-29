#In deep.py, implement a program that prompts the user for the answer to the Great 
# Question of Life, the Universe and Everything, outputting
#  Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No


lst1 = ["42","forty two","FORTY TWO","forty-two","FORTY_TWO"]
def askQuest(anss):
    if anss in lst1:
         print("yes")
    else:
        print("no")
answer=input("what is the Answer to the Great Question of life, the Universe and Everything :")
askQuest(answer)