def reverse_int(n):
    is_minus = False
    if n < 0:
        is_minus = True
        n = abs(n)

    ans = 0
    while n > 0:
        rem = n % 10
        ans = ans * 10 + rem
        n = n // 10

    if is_minus:
        ans = -ans

    return ans


n = -1
my_ans = reverse_int(n)
print(my_ans)