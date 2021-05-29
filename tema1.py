i = int()
i = 1
while (i < 1e9):
    s = str (input('Введите знак : +, -, *, /   '))
    a = int (input('Введите первое значение   '))
    b = int (input('Введите второе значение   '))
    if (s == "-"):
        print (a, ' - ', b, ' = ',a + b)
    if (s == "+"):
        print (a, ' + ', b, ' = ', a + b)
    if (s == "*"):
        print (a, ' * ', b, ' = ', a * b)
    if (s == "/"):
        if (b == 0):
            print ("Деление на 0 невозможно")
        else:
            print (a, ' / ', b, ' = ', a / b)
    a = int (input("Хотите продолжить? Если да то введите 1, иначе введите 0   "))
    if (a == 0):
        break
    else:
        continue