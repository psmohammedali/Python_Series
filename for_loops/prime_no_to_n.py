n = int(input())
for number in range(2, n + 1):
    for i in range(3, number):
        if number % i == 0:
            break
    else:
        print(number)

# for i in range(3,3):
#     print(i)
