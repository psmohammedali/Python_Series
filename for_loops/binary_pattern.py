# Sample Input :
# 5
# Sample Output :
# 11111
# 0000
# 111
# 00
# 1

def binary_pattern(n):
    for rows in range(1,n+1):
        flag = 1
        if rows %2 == 0:
            flag = 0
        for col in range(1,n-rows+2):
            print(flag,end="")
        print()
    return

n = int(input())
binary_pattern(n)
