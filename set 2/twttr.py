#When texting or tweeting, it’s not uncommon to shorten words to save time or
#  space, as by omitting vowels, much like Twitter was originally called 
# twttr. In a file called twttr.py, implement a program that prompts the user for
#  a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

newstr=""
noun=['a','e','i','o','u']
def shortenWord(str1):
    global newstr
    for i in str1:
        if i.lower() not in noun:
            newstr += i
    return newstr

in1=input("Input")
shortenWord(in1)
print(newstr)