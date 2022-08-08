def pattern(n):
    r = 1                           # r = rows
    while r <= n:
        c = 1                       # c = columns
        while c <= n:
            print(c, end="") 
            c = c + 1             # we are incrementing column value
        print()
        r = r + 1                 # we are incrementing row value
    return

n = int(input())
pattern((n)) # we are calling pattern function