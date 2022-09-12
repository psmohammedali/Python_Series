def binary_search_recursive(my_list, start, end, element):
    if (start > end) or len(list) == 0:
        return -1
    mid = (start + end) // 2
    if my_list[mid] == element:
        return mid
    if my_list[mid] > element:
        small_output = binary_search_recursive(my_list,start,mid-1,element)
        return small_output
    small_output = binary_search_recursive(my_list, mid+1, end, element)
    return small_output


list = [21,22,23,29,35,69]
print(binary_search_recursive(list,0,len(list)-1,36))