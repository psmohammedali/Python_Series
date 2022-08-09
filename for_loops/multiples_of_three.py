start = int(input())
end = int(input())

# this is okish as it runs for n times
for i in range(start,end+1,1):
    if i % 3 == 0:
        print(i)

if start%3==1:
    start = start + 2
elif start%3==2:
    start = start + 1

for i in range(start, end+1,3):
    print(i)