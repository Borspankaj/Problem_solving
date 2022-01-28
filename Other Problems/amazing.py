

l=list(map(int,input().split()))

start=0
count=0
end=1
maxx=0
while end<len(l):
    if l[end]>=maxx and l[start]>=maxx:
        maxx=max(maxx,l[end])
        
    else:
        start=end
        count+=1
        maxx=0
    end+=1
print(count) 

        


        


