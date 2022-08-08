# Character Triangle Problem

def char_triangle_pattern(n):
    r = 1
    while r <= n:
        c = 1
        w = ord("A") - 1 + r
        while c <= r:
            print(chr(w),end="")
            c = c + 1
            w = w + 1
        print()
        r = r + 1
    return


n = int(input())
char_triangle_pattern(n)
