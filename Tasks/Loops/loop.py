r=range(10)

print r

for i in r:
    print i

i=0
while(i<len(r)):
    print i
    i=i+1

s=0
l=[1,2,3,4,5,1,2,3]

for i in l:
    s=s+i
print s


i=0
s=0
while(i<len(l)):
    s=s+l[i]
    i=i+1

print s

i=-1
while(1):
    i=i+1
    if(i>5 and i<8):
       continue
    if(i>8):
        break
    print i
