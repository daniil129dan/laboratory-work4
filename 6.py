def check_perfect(num):
    factors = []
    for i in range(1,num):
        if num % i == 0:
            factors.append(i)
    if sum(factors) == num:
        print(num,': ',sum(factors) == num)
    return


for i in range(1,10001):
    check_perfect(i)
