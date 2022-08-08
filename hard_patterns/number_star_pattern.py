# Sample Input 1:
# 5
# Sample Output 1:
#            1
#           232
#          34543
#         4567654
#        567898765

def number_star_pattern(n):
    rows = 1
    # row loop
    while rows <= n:
        # space loop
        spaces = 1
        while spaces <= n-rows:
            print(" ",end="")
            spaces = spaces + 1
        # increment number loop
        temp = rows
        while temp <= ((2*rows)-1):
            print(temp,end="")
            temp = temp + 1
        temp = temp - 2   # (only once)
        while temp >= rows:
            print(temp,end="")
            temp = temp - 1
        rows = rows + 1
        print()
    return


n = int(input())
number_star_pattern(n)
