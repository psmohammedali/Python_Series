# Problem ID 91, removeConsecutiveDuplicates
def my_dup(my_string, index):
    if index == len(my_string):
        return ""
    small_string = my_dup(my_string, index + 1)
    if len(small_string) == 0 or small_string[0] != my_string[index]:
        my_output = my_string[index] + small_string
        return output

    return small_string


def removeConsecutiveDuplicates(string):
    my_ans = my_dup(string, 0)
    return my_ans


# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
