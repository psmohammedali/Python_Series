def find_number(my_list, index, element):
    if index == len(my_list):
        return -1
    if my_list[index] == element:
        return index
    small_answer = find_number(my_list,index+1, element)
    return small_answer

def find_number_slower(my_list,element):
    if len(my_list) == 0:
        return -1
    if my_list[0] == element:
        return 0
    small_ans = find_number_slower(my_list[1:],element)
    if small_ans == -1:
        return -1
    return small_ans + 1
my_list = [20,30,40,75,100]
print(find_number(my_list,0,101))
print(find_number_slower(my_list,33))
