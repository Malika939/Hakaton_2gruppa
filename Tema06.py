import random as rd
random_number = rd.randint(0,10)
sum = 0
j = 0
i = 1
for i in range(10000000):
    a = int(input('Ввеите загадонное число   '))
    if a == random_number:
        print ("Вы угадали")
        sum = 0
    else:
        sum = sum + 1
    if sum == 3:
        print ("Вы проиграли")
        break