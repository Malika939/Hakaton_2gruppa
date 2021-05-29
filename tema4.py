sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
# unique_sequense_0 = list(set(sequence_0))
# print(unique_sequense_0)
res = 0
for i in set(sequence_0):
    if sequence_0.count(i) > 1:
        print (i)
        res = 1
if res == 1:
    print ("Последовательность не уникальна", '\n')
else:
    print ("Последовательность уникальна", '\n')
res = 0
for i in set(sequence_1):
    if sequence_1.count(i) > 1:
        print (i)
if res == 1:
    print ("Последовательность не уникальна, '\n")
else:
    print ("Последовательность уникальна", '\n')
res = 0
for i in set(sequence_2):
    if sequence_2.count(i) > 1:
        print (i)
if res == 1:
    print ("Последовательность не уникальна", '\n')
else:
    print ("Последовательность уникальна", '\n')
res = 0
for i in set(sequence_3):
    if sequence_3.count(i) > 1:
        print (i)
if res == 1:
    print ("Последовательность не уникальна", '\n')
else:
    print ("Последовательность уникальна", '\n')
res = 0
