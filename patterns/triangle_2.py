# Traingle Pattern Problem

def triangle_pattern_2(n):
    r = 1
    while r <= n:
        c = 1
        while c <= r:
            print(r,end="")
            c = c + 1
        r = r + 1
        print()
    return


n = int(input())
triangle_pattern_2(n)