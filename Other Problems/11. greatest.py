l=list(map(int,input().split()))
ans=[]
n=len(l)
g=-1
if n==0 or n==1:
    print(-1)
else:
    for i in range(n-1,-1,-1):
        ans.append(g)
        if l[i]>g:
            g=l[i]
    print(ans[::-1])


