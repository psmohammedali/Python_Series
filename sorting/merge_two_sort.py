import selection_sort


def merge_two_sort(list1, list2):
    i = 0
    j = 0
    final_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            final_list.append(list1[i])
            i = i + 1
        elif list1[i] > list2[j]:
            final_list.append(list2[j])
            j = j + 1

    while i < len(list1):
        # print("list1")
        final_list.append(list1[i])
        i = i + 1

    while j < len(list2):
        # print("list2")
        final_list.append(list2[j])
        j = j + 1

    return final_list


if __name__ == "__main__":
    list1 = selection_sort.user_input()
    list2 = selection_sort.user_input()
    final_list = merge_two_sort(list1, list2)
    print(final_list)
