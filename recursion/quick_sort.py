def quick_sorting(my_list, start_index, end_index):
    if start_index >= end_index:
        return my_list
    pivot = my_list[start_index]
    count = 0
    for i in range(start_index, end_index + 1):
        if pivot > my_list[i]:
            count = count + 1
    pivot_index = start_index + count
    my_list[pivot_index], my_list[start_index] = my_list[start_index], my_list[pivot_index]
    first_pointer = start_index
    second_pointer = end_index
    while first_pointer < pivot_index < second_pointer:
        if my_list[first_pointer] > pivot:
            while second_pointer > pivot_index:
                if my_list[second_pointer] < pivot:
                    break
                second_pointer = second_pointer - 1
            my_list[first_pointer], my_list[second_pointer] = my_list[second_pointer], my_list[first_pointer]
        first_pointer = first_pointer + 1
    print(my_list)
    quick_sorting(my_list, start_index, pivot_index - 1)
    quick_sorting(my_list, pivot_index + 1, end_index)


if __name__ == "__main__":
    my_list = [3, 5, 7, 6, 10, 4, 2, 1, 4, 5]
    quick_sorting(my_list, 0, len(my_list) - 1)
    print(my_list)
