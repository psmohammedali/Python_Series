def sort_two_list(list_1, list_2):
    final_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            final_list.append(list_1[i])
            i += 1
            continue
        final_list.append(list_2[j])
        j += 1

    while i < len(list_1):
        final_list.append(list_1[i])
        i = i + 1

    while j < len(list_2):
        final_list.append(list_2[j])
        j = j + 1

    return final_list


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    list_1 = my_list[0:len(my_list) // 2]
    list_2 = my_list[len(my_list) // 2:]
    ans_1 = merge_sort(list_1)
    ans_2 = merge_sort(list_2)
    sort_list = sort_two_list(ans_1, ans_2)
    return sort_list


my_list = [3, 8, 2, 7, 1, 4, 5]
ans = merge_sort(my_list)
print(ans)
# prints [1 ,2 ,3 ,4 ,5 ,7 ,8]
