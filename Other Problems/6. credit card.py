n=input().split()
s=0
for i in range(len(n)-2,-1,-2):
    val= 2*int(n[i])
    if len(str(val))==2:
        val=int(str(val)[0]+str(val)[-1])
    s+=val
    
