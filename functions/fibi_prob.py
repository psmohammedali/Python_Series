def check_fibi(n):
    if n == 0 or n == 1:
        return True
    previous = 0
    current = 1
    while current <= n:
        if current == n:
            return True
        # print(current)
        temp = current
        current = current + previous
        previous = temp
    else:
        return False


n = int(input())
print(check_fibi(n))
