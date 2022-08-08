# Traingle Pattern Problem

def triangle_pattern(n):
    r = 0
    while(r<n):
        c = 0
        while(c<=r):
            print("*",end="")
            c = c + 1
        print(" ")
        r = r+1
    return


n = int(input())
triangle_pattern(n)
