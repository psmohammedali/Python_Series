try:
    print(y)
    x = 5/0

    print(x)
except NameError:
    print("There is an error in the code")
except ZeroDivisionError:
    print("This is zero division error")
