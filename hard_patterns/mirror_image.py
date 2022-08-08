# Pattern for N = 4
#    1
#   12
#  123
# 1234

def mirror_image_pattern(n):
    outer_loop = 1
    while outer_loop <= n:
        space_column = n - outer_loop
        j1 = 1
        while j1 <= space_column:
            print(" ",end="")
            j1 = j1 + 1
        j1 = 1
        while j1 <= outer_loop:
            print(j1, end="")
            j1 = j1 + 1
        outer_loop = outer_loop + 1
        print()
    return


n = int(input())
mirror_image_pattern(n)
