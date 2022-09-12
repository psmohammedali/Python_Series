def pn(n):
    if n == 1:
        print(n)
        return
    pn(n - 1)
    print(n)
    return


n = int(input())
pn(n)
