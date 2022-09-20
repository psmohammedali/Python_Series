def insertion_sort(my_list):
    if len(my_list) == 1:
        return my_list
    length = len(my_list)
    for i in range(1,length):
        current_element = my_list[i]
        j = i - 1
        while j >= 0:
            if my_list[j]>current_element:
                my_list[j+1] = my_list[j]
                j = j - 1
            else:
                break
        my_list[j+1] = current_element


if __name__ == "__main__":
    my_list = [5, 4, 5, 1, 7, 2, 6]
    insertion_sort(my_list)
    print(my_list)
