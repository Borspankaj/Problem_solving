l=[0,1,2,3,0,4,2]

val=2
p=count=0
for i in range(len(l)):
    if val==l[p]:
        l.remove(val)
        l.append('_')
        count+=1
    else:
        p+=1
print(len(l)-count)
