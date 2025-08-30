'''In a file called extensions.py, 
implement a program that prompts the user for the name of a file 
and then outputs that file’s media type if the file’s name ends, case-insensitively, 
in any of these suffixes:'''

def findExtension(ext):
    if ext.endswith(".jpeg") or ext.endswith(".jpg"):
        print("images/jpeg")
    elif ext.endswith(".gif"):
        print("image/gif")
    elif ext.endswith(".zip"):
        print("file/zip")
    elif ext.endswith(".txt"):
        print("file/txt")
ext=input("enter file name with extension")
findExtension(ext)