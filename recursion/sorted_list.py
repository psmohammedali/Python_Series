def sorted_or_not(my_list,n):
    if n == len(my_list)-1:
        return True
    # if len(my_list) in [0, 1]:
    #     return True

    start = n
    next = n + 1
    if my_list[start] <= my_list[next]:
        print(n+1)
        small_ans = sorted_or_not(my_list,n+1)
        return small_ans

    return False


if __name__ == "__main__":
    my_list = [4,6,7]
    ans = sorted_or_not(my_list,0)
    print(ans)
