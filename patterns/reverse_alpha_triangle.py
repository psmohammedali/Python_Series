# Reverse Alpha Triangle Pattern Problem

def reverse_char_pattern(n):
    r = 0
    while r < n:
        c = 0
        p = ord("A") - 1 + n - r
        while c <= r:
            print(chr(p),end="")
            c = c + 1
            p = p + 1
        print()
        r = r + 1
    return


n = int(input())
reverse_char_pattern(n)