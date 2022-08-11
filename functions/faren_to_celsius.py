
def faren_to_cel(temp):
    cel_value = ((temp - 32) * 5)/9
    return int(cel_value)

def faren_to_cel_range(start,end, step):
    for i in range(start,end,step):
        print(i," ",faren_to_cel(i))
    pass


faren_s = int(input())
faren_e = int(input())
step = int(input())
faren_to_cel_range(faren_s,faren_e+1,step)