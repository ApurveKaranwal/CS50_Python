def main():
    str1=input("Word: ")
    new=shorten(str1)
    print(new)

def shorten(word):
    s1=""
    for i in word:
        if i.lower() not in ['a','e','i','o','u']:
            s1=s1+i
    return s1

if __name__ == "__main__":
    main()