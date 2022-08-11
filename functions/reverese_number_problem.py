def reverse_num(n):
    result = 0
    while n > 0:
        rem = n % 10
        result = 10*result + rem
        n = n // 10

    return result


n = int(input())
ans = reverse_num(n)
print(ans)