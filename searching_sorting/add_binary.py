def addBinary(a, b):
    result_string = ""
    if len(a) >= len(b):
        top = a
        bottom = b
    else:
        top = b
        bottom = a

    i = len(top) - 1
    j = len(bottom) - 1

    rem = 0
    while i >= 0:
        if j >= 0:
            j_value = int(bottom[j])
        else:
            j_value = 0
        add_up = int(top[i]) + j_value + rem
        rem = add_up // 2
        dividend = add_up % 2
        result_string = str(dividend) + result_string
        i = i - 1
        j = j - 1

    if rem != 0:
        result_string = str(rem) + result_string

    return result_string


a = "1101"
b = "1"
my_string = addBinary(a,b)
print(my_string)