lis=[1,3,4,5,2,2]
def solve(lis):
    s=sum(lis)
    s_=0
    for i in range(len(lis)):
        s-=lis[i]
        if s_==s:
            return i+1
        s_+=lis[i]
    return -1

print(solve(lis))