a = []

line = str(input("Введите число (Enter для завершения): "))
while line != "":
    a.append(line)
    line = input("Введите число (Enter для завершения): ")

a = list(set(a))

for i in range(len(a)):
    print(a[i])