l=list(map(int,input().split()))

start=0
end=1
while end<len(l):
    if l[end]==l[start]:
        l.remove(l[start])
    

    else:
        start+=1
        end+=1

print(l)