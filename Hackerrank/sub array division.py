l=[2,2,1,3,2]
d=4
m=2

def solve(l,d,m):
    count=s=0
    for i in range(m):
        s+=l[i]
    count+=1 if s==d else 0
    start=0
    end=m
    while end<len(l):
        s=s-l[start]+l[end]
        if s==d:
            count+=1
        end+=1
        start+=1

    return count
        

print(solve(l,d,m))