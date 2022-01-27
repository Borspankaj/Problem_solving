l=[3, 4, 2,5, 1]
l1=l[:]
c1=c2=0
for i in range(len(l)):
    small=i
    
    for j in range(i+1,len(l)):
        if l[small]>l[j]:
            small=j
    if small!=i:
        l[small],l[i]=l[i],l[small]
        c1+=1

for i in range(len(l)):
    g=i
    
    for j in range(i+1,len(l)):
        if l[g]<l[j]:
            g=j
    if g!=i:
        l[g],l[i]=l[i],l[g]
        c2+=1
print(min(c1,c2))
    

   