numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
i = 0
for i in range (len(numbers)):
    if (numbers[i] > numbers[i - 1]):
        print (numbers[i])