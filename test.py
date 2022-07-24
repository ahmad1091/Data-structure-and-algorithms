def sumOf(**kwargs):
    print(kwargs)
    sum = 0
    for x,k in kwargs.items():
        sum += x
    return sum

print(sumOf(all=1.5,ball=5.2))