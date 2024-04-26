while True:
    n = int(input("enter the number of rows: "))

    for i in range(n):
        print(" "*(n-i-1), end=" ")
        print("*"*(i+1))
    break