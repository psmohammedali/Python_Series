def increment(a):
    print("Increment function before :",id(a))
    a = a + 5
    print("Increment function after :", id(a))

a = 7
print("main function before :", id(a))
increment(a)
print("main function after :", id(a))