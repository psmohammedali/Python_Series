def check_sequence(n):
    previous = int(input())
    if n == 1:
        return True
    current = 0
    is_decreasing = True
    i = 1
    while i <= n - 1:
        current = int(input())
        if previous > current and is_decreasing == True:
            pass
        elif current > previous and is_decreasing == True:
            is_decreasing = False
            pass

        elif current > previous and is_decreasing == False:
            pass
        else:
            return False

        previous = current
        i = i + 1
    else:
        return True


n = int(input())
ans = check_sequence(n)
print(ans)
