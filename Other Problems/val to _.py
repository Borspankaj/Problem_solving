l=[0,1,2,3,0,4,2]

val=2
p=0
for i in range(len(l)):
    if val==l[p]:
        l.remove(val)
        l.append('_')
    else:
        p+=1
print(l)
