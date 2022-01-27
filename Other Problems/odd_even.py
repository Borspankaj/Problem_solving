l=list(map(int,input().split()))
last=0
for i in range(len(l)):
    if l[i]%2==0:
        last+=1
    else:
        break
p=last
while p<len(l):
    if l[p]%2==0:
        val=l[p]
        del l[p]
        l.insert(last,val)
        last+=1 
    p+=1

print(l)

