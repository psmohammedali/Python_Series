def selection_sort(my_list):
    if len(my_list) == 1:
        return my_list
    for i in range(len(my_list) - 1):
        smallest_value_index = i
        # for comparing all elements next to i
        for j in range(i + 1, len(my_list)):
            if my_list[smallest_value_index] > my_list[j]:
                smallest_value_index = j

        # At this point, I got the smallest value that can fit in index-i
        my_list[i], my_list[smallest_value_index] = my_list[smallest_value_index], my_list[i]


if __name__ == "__main__":
    my_list = [5, 4, 3, 1, 7, 2, 6]
    selection_sort(my_list)
    print(my_list)
