def system_depth(n):
    if n == 998:
        return
    print(n)
    system_depth(n+1)

system_depth(1)