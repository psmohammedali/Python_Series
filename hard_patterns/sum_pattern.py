# Sample Input 2 :
#  5
# Sample Output 2 :
# 1=1
# 1+2=3
# 1+2+3=6
# 1+2+3+4=10
# 1+2+3+4+5=15

def sum_pattern(n):
    i = 1

    while i <= n:
        total = 0
        col = 1
        while col <= i:
            print(col,end="")
            total = total + col
            if col < i:
                print("+",end="")
            col = col + 1
        print("=",end="")
        print(total)
        i = i + 1


n = int(input())
sum_pattern(n)