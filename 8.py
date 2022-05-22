x = []
y = []

xi = input("Введите X: ")
yi = input("Введите Y: ")
n = 1
b = 0
m = 0

while xi != '':
    xf = float(xi)
    yf = float(yi)
    x.append(xf)
    y.append(yf)

    xi = input("Введите X (Enter для завершения): ")
    if xi != '':
        yi = input("Введите Y: ")
        n += 1
sumxy = float()
sumsqrx = float()

for i in range(len(x)):
    sumxy = x[i]*y[i] + sumxy

for i in range(len(x)):
    sumsqrx = x[i]**2 + sumsqrx

sumxy = round(sumxy,1)
sumsqrx = round(sumsqrx,1)

print(sumxy, sumsqrx, sum(x), sum(y), n)

m = round((sumxy - (sum(x)*sum(y))/n)/(sumsqrx-sum(x)**2/n), 2)
b = round(sum(y)/n - m * (sum(x)/n), 2)

if b > 0:
    print('Итоговая функция равна: y = ', m, '* x +', b)
else:
    print('Итоговая функция равна: y = ', m, 'x', b)