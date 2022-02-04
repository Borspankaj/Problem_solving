l=list(map(int,input().split()))
minn=maxx=l[0]
recm=recmi=0
for i in l:
    if i>maxx:
        maxx=i
        recm+=1

    if i<minn:
        recmi+=1
        minn=i

print([recm,recmi])