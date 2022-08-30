def binary_searching(my_list, element):
    start = 0
    end = len(my_list) - 1
    while start <= end:
        mid = (start + end) // 2  # Integer Division
        if my_list[mid] < element:
            start = mid + 1
        elif my_list[mid] > element:
            end = mid - 1
        else:
            return mid  # my_list[mid] == element
    else:
        return -1


if __name__ == "__main__":
    my_list = [1, 4, 6, 8, 9, 10, 14, 17, 18]
    element = 19
    ans = binary_searching(my_list, element)
    print(ans)
