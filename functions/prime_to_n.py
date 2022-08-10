def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def prime_to_n(n):
    for i in range(2,n+1):
        i_is_prime = isprime(i)
        if i_is_prime:
            print(i)


n = int(input())
prime_to_n(n)
