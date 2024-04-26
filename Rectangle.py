#How many rows do u need to print
while True:
    n = int(input("Number of rows: "))
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print("\n")