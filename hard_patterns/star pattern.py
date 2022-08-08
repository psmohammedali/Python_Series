# Star Pattern
def star_pattern(n):
    rows = 1
    while rows <= n:
        spaces = 1
        # Space loop
        while spaces <= n-rows:
            print(" ",end="")
            spaces = spaces + 1
        # Star loop
        stars = 1
        while stars <= ((2*rows)-1):
            print("*",end="")
            stars = stars + 1
        print()
        rows = rows + 1
    return


n = int(input())
star_pattern(n)