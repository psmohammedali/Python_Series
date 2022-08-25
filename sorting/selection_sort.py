def selection_sorting(my_list):
    # One kind of edge case
    if len(my_list) <= 1:
        return my_list
    i = 0
    while i < len(my_list) - 1:
        smallest = i
        j = i + 1
        while j < len(my_list):
            # Checking values with respective indices
            if my_list[j] < my_list[smallest]:
                smallest = j
            j = j + 1

            # Swapping
        my_list[i], my_list[smallest] = my_list[smallest], my_list[i]
        i = i + 1


def user_input():
    n = int(input())
    user_list = [int(i) for i in input().split()]
    return user_list


if __name__ == "__main__":
    my_list = user_input()
    print(id(my_list))
    selection_sorting(my_list)
    print(my_list)
    print(id(my_list))
