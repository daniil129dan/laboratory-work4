a = []

line = int(input("Введите число (0 для завершения): "))

while line != 0:
    a.append(line)
    line = int(input("Введите число (0 для завершения): "))

a = sorted(a)

for i in range(len(a)):
    print(a[i])