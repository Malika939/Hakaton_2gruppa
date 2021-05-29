spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
i = 0
ln = len (spisok_1)
for i in range (ln):
    if (spisok_1[i] != spisok_2[i]):
        print (spisok_1[i])