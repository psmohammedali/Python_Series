import sys


def take_input():
    num_length = int(input())
    my_list = [int(x) for x in input().strip().split()]
    return my_list, num_length


def linear_search(my_list, to_find) -> int:
    for inx, val in enumerate(my_list):
        if val == to_find:
            return inx
    else:
        return -1


n = int(input())

while n > 0:
    num_list, num_length = take_input()
    to_find = int(input())
    index = linear_search(num_list, to_find)
    print(index)
    n = n - 1
