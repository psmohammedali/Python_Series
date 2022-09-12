def my_sumArray(my_list,index):
    if index == len(my_list):
        return 0
    small_output = my_sumArray(my_list,index + 1)
    my_ouput = my_list[index] + small_output
    return my_output

def sumArray(arr):
    my_ans = my_sumArray(arr,0)
    return my_ans

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
