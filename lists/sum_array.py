def get_input(n):
    input_list = []
    for i in range(n):
        temp = list(map(int, input().rstrip().split(" ")))
        print(type(temp))
        print(temp)
        input_list.append(temp)
    return input_list


n = int(input())
in_list = get_input(n)
print(in_list)
