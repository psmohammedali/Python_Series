## Read input as specified in the question.
## Print output as specified in the question.
def str_to_int(my_str):
    # print(my_str)
    if len(my_str) == 1:
        return int(my_str)
    last_digit = int(my_str[-1])
    print(my_str)
    small_ans = str_to_int(my_str[0:len(my_str)-1])
    my_ans = 10*small_ans + last_digit
    print('HI')
    return my_ans



my_input = input()
ans = str_to_int(my_input)
print(ans)