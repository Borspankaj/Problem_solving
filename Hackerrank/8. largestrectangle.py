h = [11,11,10,10,10]
def solve(h):
    nsel=[]
    nser=[]
    stack=[]
    for i in range(len(h)):
        while stack and stack[-1][0]>=h[i]:
            stack.pop()
                
        if not stack:
            nsel.append(-1)
        else:
            nsel.append(stack[-1][1])
        stack.append([h[i],i])

    
    stack=[]
    n=len(h)
    for i in range(n-1,-1,-1):
        while stack and stack[-1][0]>=h[i]:
            stack.pop()

        if not stack:
            nser.append(n)

        else:
            nser.append(stack[-1][1])

        stack.append([h[i],i])
    nser.reverse()

    maxx=0
    for i in range(n):
        area=(nser[i]-nsel[i]-1)*h[i]
        print(area)
        maxx=max(area,maxx)

    return maxx
        
print(solve(h))    
