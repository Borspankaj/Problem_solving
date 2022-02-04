l=[1,0,0,2,3,0]
i=0
while i<len(l):
    if l[i]==0:
        l.insert(i+1,0)
        l.pop()
        i+=2
    else:
        i+=1


print(l)