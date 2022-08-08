# Sample Input 1:
# 5

# Sample Output 1:
#   *
#  ***
# *****
#  ***
#   *
def star_pattern(n):
    n1 = n // 2 + 1
    n2 = n - n1

    # First Half Pattern
    rows = 1
    while rows <= n1:
        spaces = 1
        # Space Loop
        while spaces <= n1 - rows:
            print(" ", end="")
            spaces = spaces + 1

        # Star Loop
        stars = 1
        while stars <= ((2 * rows) - 1):
            print("*", end="")
            stars = stars + 1

        rows = rows + 1
        print()

        # Second Half Pattern
    rows = 1
    while rows <= n2:

        # Space Loop
        spaces = 1
        while spaces <= rows:
            print(" ", end="")
            spaces = spaces + 1

        # Star Loop
        stars = 1
        while stars <= 2*(n2-rows+1)-1:
            print("*", end="")
            stars = stars + 1

        rows = rows + 1
        print()
    return


n = int(input())
star_pattern(n)
