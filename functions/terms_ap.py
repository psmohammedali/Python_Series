# Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.

n = int(input())
i = 1
p = 1
while i <= n:
    ap_format = 3*p+2
    if ap_format % 4 == 0:
        p = p + 1
        continue
    print(ap_format)
    i = i + 1
    p = p + 1

