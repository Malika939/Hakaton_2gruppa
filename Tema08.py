numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
chet = 0
nechet = 0
i = 0
for i in range (len(numbers)):
    if numbers[i] % 2 == 0:
        chet = chet + 1
    else:
        nechet = nechet + 1
print (chet, " четных чисел")
print (nechet, " нечетных чисел")