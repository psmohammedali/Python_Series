def binary_searching(my_list, element):
    i = 0
    while i < len(my_list):
        if my_list[i] == element:
            return i
        i = i + 1
    else:
        return -1


if __name__ == "__main__":
    my_list = [7, 2, 0, 7, 2, 3, 5, 9, 5]
    element = 3
    idx = binary_searching(my_list, element)
    print(idx)
