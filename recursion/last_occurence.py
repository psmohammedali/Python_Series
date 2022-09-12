def last_occurence(my_list, index, ele):
    if index == len(my_list):
        return -1
    my_answer = last_occurence(my_list,index+1,ele)
    if my_answer == -1:
        if my_list[index] == ele:
            return index
        else:
            return -1
    return my_answer

def last_occurence_slower(my_list, ele):
    if len(my_list) == 0:
        return -1
    small_output = last_occurence_slower(my_list[1:],ele)
    if small_output == -1:
        if my_list[0] == ele:
            return 0
        else:
            return -1
    return small_output + 1


    pass

my_list = [11,22,33,44,55,11,22,33,44,55,33,22]
print(last_occurence(my_list,0,44))
print(last_occurence_slower(my_list,44))s