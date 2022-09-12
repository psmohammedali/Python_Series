
def luckyNumbers(matrix) :
    my_list = []
    i = 0
    while i < len(matrix):
        row = i
        col = 0
        j = 0
        current_low = matrix[i][j]
        while j < len(matrix[i]):
            if current_low > matrix[i][j]:
                current_low = matrix[i][j]
                col = j
            j = j + 1

        # Searching in + direction
        search_row = 0
        while search_row < len(matrix):
            if matrix[search_row][col] > current_low:
                break
            search_row = search_row + 1
        else:
            my_list.append(current_low)

        i = i + 1

    print(my_list)


matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
luckyNumbers(matrix)