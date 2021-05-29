a = []
n = int()
for i in range (300):
    n = input()
    a[i] = n
i = 0
for i in range (300):
    a = int (input())
    if (a[i] % 2 == 0):
        print (a)
    else:
        if (a[i] == 237):
            break
        else:
            continue