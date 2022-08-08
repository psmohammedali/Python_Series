# Pattern for N = 4
# 4444
# 333
# 22
# 1

def inverted_pattern(n):
    rows = 1
    while rows <= n:
        col = 1
        while col <= n - rows + 1:
            print(n - rows + 1, end="")
            col = col + 1
        rows = rows + 1
        print()
    return

n = int(input())
inverted_pattern(n)