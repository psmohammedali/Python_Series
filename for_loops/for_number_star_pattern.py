def number_pattern(n):
    for rows in range(1, n + 1):
        # Space loop
        for spaces in range(1, n-rows+1):
            print(" ", end="")
        # Increment number loop
        for num in range(rows, 2 * rows):
            print(num, end="")
        # Decrement number loop
        for num in range(2 * rows - 2, rows - 1, -1):
            print(num, end="")
        print()
    return


n = int(input())
number_pattern(n)
