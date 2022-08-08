# Sample Input 2 :
# 5
# Sample Output 2 :
# *****
#  *****
#   *****
#    *****
#     *****

def parallelogram(n):
    i = 1
    while i <= n:
        spaces = 1
        while spaces <= i-1:
            print(" ",end="")
            spaces = spaces + 1
        stars = 1
        while stars <= n:
            print("*",end="")
            stars = stars + 1
        i = i+1
        print()
    return


n = int(input())
parallelogram(n)
