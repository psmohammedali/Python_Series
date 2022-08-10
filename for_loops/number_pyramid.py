# for n = 5
# output
# 12345
#  2345
#   345
#    45
#     5
#    45
#   345
#  2345
# 12345

def number_pyramid(n):
    # first half pattern

    for i in range(1,n+1):
        # space loop
        for spaces in range(1,i):
            print(" ",end="")
        # number loop
        for num in range(i,n+1):
            print(num,end="")
        print()
   # Second half pattern
    n2 = n - 1
    for i in range(1,n):
        # space loop
        for spaces in range(1,n2-i+1):
            print(" ",end="")
        # number loop
        for num in range(n2-i+1,n+1):
            print(num,end="")
        print()







n = int(input())
number_pyramid(n)