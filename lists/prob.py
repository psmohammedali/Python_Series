a = [1,2,3]
b = []
print("before work")
print(id(a))
print(id(b))

b = a
print("before work")
print(id(a))
print(id(b))

a[1] = 5
print(a)
print(b)
print(id(a))
print(id(b))