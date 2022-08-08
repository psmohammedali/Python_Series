def inverted_pattern(n):
    rows = 1
    while rows <= n:
        columns = n - rows + 1
        j = 1
        while j <= columns:
            print(j, end="")
            j = j + 1
        rows = rows + 1
        print()
    pass




n = int(input())
inverted_pattern(n)