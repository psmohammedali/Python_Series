import selection_sort


def insertion_sorting(my_list):
    n = len(my_list)
    for i in range(1,n):
        j = i - 1
        current = my_list[i]
        while j >= -1:
            if j == -1:
                my_list[j+1] = current
                break
            if my_list[j] > current:
                my_list[j+1] = my_list[j]
            elif my_list[j] <= current:
                my_list[j+1] = current
                break
            j = j - 1
    pass


if __name__ == "__main__":
    my_list = selection_sort.user_input()
    insertion_sorting(my_list)
    print(my_list)