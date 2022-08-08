def reverse_triangle(n):
    r = 1
    while r <= n:
        c = r
        while c >= 1:
            print(c, end="")
            c = c - 1
        r = r + 1
        print()

    return


n = int(input())
reverse_triangle(n)
