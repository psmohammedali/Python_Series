def print_n(n):
    if n == 0:
        return
    print_n(n-1)
    print(n)

print_n(9)
