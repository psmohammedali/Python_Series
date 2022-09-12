# first_string = [int(x) for x in input().strip().split()]
# row,col = first_string[0] , first_string[1]
# input_two_dim = []
# for i in range(row):
#     row_list = [int(num) for num in input().strip().split()]
#     input_two_dim.append(row_list[:col])
#
# # Print input list
# for i in input_two_dim:
#     for j in i:
#         print(j, end=" ")
#     print()


li = [int(j) for j in range(5) for i in range(4)]
li2 = []
li3 = [[int(j) for j in range(5)] for i in range(4)]

for j in range(5):
    for i in range(4):
        li2.append(j)
print(li)
print(li2)
print(li3)
