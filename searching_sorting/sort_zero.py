from sys import stdin


def sortZeroesAndOne(arr,n):
    first_pointer = 0
    last_pointer = n-1
    while first_pointer < last_pointer:
        if arr[first_pointer] == 0:
            first_pointer = first_pointer + 1
            continue
        if arr[first_pointer] == 1:
            while arr[last_pointer] == 1:
                if last_pointer <= first_pointer:
                    break
                last_pointer = last_pointer - 1
            arr[first_pointer],arr[last_pointer] = arr[last_pointer],arr[first_pointer]


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
