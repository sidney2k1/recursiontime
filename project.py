def xyz(n):
    n=int(input("Enter a number:"))
    if n>1:
        print("Im a positive number")
        xyz(n)
    elif n==0:
        print("Im zero")
        xyz(n)
    else:
        print("im a negative number")
xyz(0)