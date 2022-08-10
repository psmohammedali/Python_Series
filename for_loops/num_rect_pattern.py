def number_pattern(n):
    # first half pattern
    total_rows = (2 * n) - 1
    n1 = total_rows // 2
    i = 1
    while i <= n1:
        # Decrement loop from n
        col = 1
        p = n
        while col <= i:
            print(p, end="")
            p = p - 1
            col = col + 1

        # repetitive loop
        col = 1
        p = n1 - i + 2
        while col <= (2 * (n1 - i) + 1):
            print(p, end="")
            col = col + 1

        # Increment loop from __ to n
        col = 1
        p = n1 - i + 2
        while col <= i:
            print(p, end="")
            p = p + 1
            col = col + 1
        print()
        i = i + 1

    # Second half Pattern
    p = n
    col = 1
    while col <= n:
        print(p, end="")
        col = col + 1
        p = p - 1

    col = 1
    p = 2
    while col <= n - 1:
        print(p, end="")
        col = col + 1
        p = p + 1
    print()

    n2 = n1
    # Third Half pattern
    i = 1
    while i <= n2:
        # Decrement loop from n
        col = 1
        p = n
        while col <= n2 - i + 1:
            print(p, end="")
            p = p - 1
            col = col + 1

        # Repetitive loop
        col = 1
        while col <= (2 * i - 1):
            print(i + 1, end="")
            col = col + 1

        # Increment loop
        col = 1
        p = i + 1
        while col <= (n2 - i + 1):
            print(p, end="")
            col = col + 1
            p = p + 1

        i = i + 1
        print()


n = int(input())
number_pattern(n)
