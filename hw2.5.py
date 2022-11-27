import math
a=input()

b=0
c=0

for i in reversed(range(0, len(a))):
    b+=(int(a[i]) * int(math.pow(2,c)))
    c+=1

print(b)
