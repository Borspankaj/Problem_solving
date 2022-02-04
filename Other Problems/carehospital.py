d={'P':'Pediatrics','O':'Orthopedics','E':'ENT'}

arr=list(map(int,input().split()))
p,o,e=0,0,0
for i in arr:
    if i=='P':
        p+=1

    elif i=='O':
        o+=1

    elif i=='E':
        e+=1
if p>o and p>e:
    print(d['P'])
elif o>p and o>e:
    print(d['O'])
else:
    print(d['E'])