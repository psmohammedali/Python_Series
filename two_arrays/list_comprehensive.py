li = ["my", "name", "is", 'billa']
new_li = [[i for i in word] for word in li]
for i in new_li:
    for j in i:
        print(j, end=" ")
    print()
