def nth_fibi(n):
    if n == 0 or n == 1:
        return n
    previous = 0
    current = 1
    for i in range(2,n+1):
        temp = current
        current = current + previous
        previous = temp
    return current

n = int(input())
ans = nth_fibi(n)
print(ans)
