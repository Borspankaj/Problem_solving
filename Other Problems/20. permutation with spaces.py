s="abcd"
i=1
def solve(s,st,i):
    if i==len(s):
        print(st)
        return
    solve(s,st+s[i],i+1)
    solve(s,st+"_"+s[i],i+1)


solve(s,s[0],i)  
