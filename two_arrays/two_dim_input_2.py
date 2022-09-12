# 3 4
# 1 2 3 4 5 6 7 8 9 10 11 12
input_string = input().split()
row = int(input_string[0])
col = int(input_string[1])
line_string = input().split()
output_string = []
j = 0
for i in range(row):
    output_string.append([line_string[j:j+col]])
    j = j + col

print(output_string)



