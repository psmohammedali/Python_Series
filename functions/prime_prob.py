def prime_function(n):
    for i in range(1,n):
        if n % i == 0:
            return False
    else:
        return True


n = int(input())
ans = prime_function(n)
print(ans)
if ans:
    print("{} is a prime number".format(n))
else:
    print("%d is not a prime number" %n)

