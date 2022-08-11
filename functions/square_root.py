def square_root(n):
    i = 0
    while i**2 <= n:
        if i**2 == n:
            return i
        i = i + 1
    return i - 1
    pass


n = int(input())
ans = square_root(n)
print(ans)
