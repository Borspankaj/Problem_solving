b="011001"
r=[-1]
for i,char in enumerate(b):
    if char=='0':
        r.append(i)
r.append(len(b))

maxx=0
for i in range(1,len(r)-1):
    maxx=max(maxx,(r[i]-r[i-1])+(r[i+1]-r[i])-1)
print(maxx)