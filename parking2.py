testcases = int(input())
while testcases > 0:
    stores = int(input())
    x = input()
    x = [int(i) for i in x.split()]
    print((max(x)-(min(x)))*2)
    testcases -= 1