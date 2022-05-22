a = []

line = input("Введите число (Enter для завершения): ")

while line != "":
    n = int(line)
    a.append(n)
    line = input("Введите число (Enter для завершения): ")

for i in range(len(a)):
    if a[i] < 0:
        print(a[i])

for i in range(len(a)):
    if a[i] == 0:
        print(a[i])

for i in range(len(a)):
    if a[i] > 0:
        print(a[i])
