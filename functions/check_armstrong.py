def is_armstrong(n):
    temp = n
    result = 0
    while temp > 0:
        rem = temp % 10
        result = rem**3 + result
        temp = temp//10
    if n == result:
        return True
    return False


n = int(input())
print(is_armstrong(n))