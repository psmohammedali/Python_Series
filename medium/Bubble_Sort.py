def bubble_sort(my_list):
    if len(my_list) == 1:
        return my_list

    length = len(my_list)
    for i in range(length - 1):
        j = 0
        end_index = length - i - 1
        while j < end_index:
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            j = j + 1
        print(my_list)


if __name__ == "__main__":
    my_list = [5, 4, 3, 1, 7, 2, 6]
    bubble_sort(my_list)
    print(my_list)
