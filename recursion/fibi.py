def fibinoci(n):
    if n == 0 or n == 1:
        return n
    smallOutput1 = fibinoci(n-1)
    smallOutput2 = fibinoci(n-2)
    print(smallOutput1 + smallOutput2)
    return smallOutput1 + smallOutput2
print(fibinoci(10))