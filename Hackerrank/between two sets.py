a=[2,4]
b=[16,32,96]

multiples=[]

for i in sorted(a,reverse=True):
    val=1
    counter=1
    m=set()
    while True:
        val=counter*i
        m.add(i*counter)
        counter+=1
        if val>=min(b):
            break
    multiples.append(m)

inter=list(set.intersection(*multiples))

count=0
for i in inter:
    flag=0
    for j in b:

        if j%i!=0:
            flag=1
            break
    if flag==0:
        count+=1
        
        
print(count)



