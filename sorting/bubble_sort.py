import selection_sort


def bubble_sorting(my_list):
    # for i in range(len(my_list) - 1):
    #     for j in range(len(my_list) - i - 1):
    #         if my_list[j] > my_list[j + 1]:
    #             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    i = 0
    length = len(my_list)
    while i < length - 1:
        j = 0
        while j < length - i - 1:
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            j = j + 1
        i = i + 1


if __name__ == "__main__":
    my_list = selection_sort.user_input()
    bubble_sorting(my_list)
    print(my_list)
