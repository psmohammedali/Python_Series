def binary_to_decimal(n):
    result = 0
    power_number = 0
    while n > 0:
        rem = n % 10
        result = result + (rem * (2 ** power_number))

        n = n // 10
        power_number = power_number + 1

    return result


n = int(input())
ans = binary_to_decimal(n)
print(ans)
