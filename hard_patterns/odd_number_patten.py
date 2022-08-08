# Sample Input 2 :
#  5
# Sample Output 2 :
# 13579
# 35791
# 57913
# 79135
# 91357
def odd_num_pattern(n):
    i = 1
    while i <= n:
        p = i
        col = 1
        while col <= n - i + 1:
            print(2*p-1, end="")
            p = p + 1
            col = col + 1
        col = 1
        while col <= i-1:
            print(2*col - 1,end="")
            col = col + 1
        i = i+1
        print()

    return

n = int(input())
odd_num_pattern(n)