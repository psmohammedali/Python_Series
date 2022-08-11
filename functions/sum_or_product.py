def add_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


def product_n(n):
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total


n = int(input())
c = int(input())
if c == 1:
    print(add_n(n))
elif c == 2:
    print(product_n(n))
else:
    print(-1)
