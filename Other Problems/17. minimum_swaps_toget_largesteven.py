n=list(map(int(input().split())))
def get_max(n):
    idx=0
    maxx=0
    for i in range(n):
        if maxx<=n[i]:
            idx=i
            maxx=n[i]
    return idx

if n[-1]%2==0:
    idx=get_max(n[:-1])
    n[0],n[idx]=n[idx],n[0]


