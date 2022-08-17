from sys import stdin


def pairSum(arr, n, x):
    arr.sort()
    print(arr)
    count = 0
    first_pointer = 0
    last_pointer = n - 1

    # Corner case - when length of the list is 1 or empty list
    if first_pointer >= last_pointer:
        return count

    while first_pointer != last_pointer:

        if arr[first_pointer] + arr[last_pointer] > x:
            last_pointer = last_pointer - 1
            while arr[first_pointer] + arr[last_pointer] <= x or first_pointer == last_pointer:
                if first_pointer == 0:
                    break
                first_pointer = first_pointer - 1
            continue

        if arr[first_pointer] + arr[last_pointer] < x:
            first_pointer = first_pointer + 1
            continue

        if arr[first_pointer] + arr[last_pointer] == x:
            count = count + 1
            first_pointer = first_pointer + 1
            continue

    return count


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1

