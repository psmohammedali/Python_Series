# Sample Input 1 :
# 4
# Sample Output 1 :
# *
# *1*
# *121*
# *12321*
# *1234321*
# *12321*
# *121*
# *1*
# *

def half_diamond_pattern(n):

    # First Half Pattern
    print("*")
    n1 = n
    i = 1
    while i <= n1:
        print("*",end="")
        col = 1
        while col <= i:
            print(col,end="")
            col = col + 1
        col = i -1
        while col >= 1:
            print(col,end="")
            col = col - 1
        i = i + 1
        print("*")

    n2 = n - 1
    i = 1
    while i <= n2:
        print("*",end="")
        col = 1
        while col <= n2 - i + 1:
            print(col, end="")
            col = col + 1
        col = n2 - i
        while col >= 1:
            print(col, end="")
            col = col - 1
        i = i + 1
        print("*")

    print("*")
    return



n = int(input())
half_diamond_pattern(n)
