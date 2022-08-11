
def dec_to_binary(n):
    result = 0
    power = 0
    while n > 0:
        rem = n %2
        result = result + (rem * (10**power))
        power = power + 1
        n = n//2

    return result


n = int(input())
ans = dec_to_binary(n)
print(ans)

