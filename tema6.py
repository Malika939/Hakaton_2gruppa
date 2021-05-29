n = int (input())
a = n // 1000 % 10
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
if (a == b + 1 and b == c + 1 and c == d + 1):
   print ("Да")
else:
   print ("Нет")