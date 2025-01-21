def headrec(n,num):
    #base case if n exceeds num terminate the recursion
    if n>num:
        return
    headrec(n+1,num)
    #print the current value of n after returning from the recursive call
    print(n)
n=int(input("Enter the number:"))
headrec(1,n)