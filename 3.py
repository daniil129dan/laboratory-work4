def maxmin(b):
    b.remove(max(b))
    b.remove(min(b))
    return b

a = []
line = int(input("Введите число (0 для завершения): "))

while line != 0:
    a.append(line)
    line = int(input("Введите число (0 для завершения): "))

print(a)
print(maxmin(a))
