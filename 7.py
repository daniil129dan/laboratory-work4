a = []

line = input("Введите число (Enter для завершения): ")
count = 0
average = 0

while line != "":
    n = float(line)
    a.append(n)
    line = input("Введите число (Enter для завершения): ")
    count +=1
    average += n

average = average / count

b = []
for i in range(len(a)):
    if a[i] < average:
        b.append(a[i])
c = []
for i in range(len(a)):
    if a[i] == average:
        c.append(a[i])
d = []
for i in range(len(a)):
    if a[i] > average:
        d.append(a[i])
print('Список: ', a)
print('Среднее значение списка: ', average)

if len(b) > 0:
    print('Числа меньше среднего значение: ', b)

if len(c) > 0:
    print('Числа равные среднему значению: ', c)

if len(d) > 0:
    print('Числа больше среднего значения: ', d)

