h=[18,1,2,1,6,4,2]
nger=[]
stack=[]
for i in range(len(h)-1,-1,-1):
    while stack and stack[-1]>=h[i]:
        stack.pop()
    if not stack:
        nger.append(-1)
    else:
        nger.append(stack[-1])
    stack.append(h[i])


nger.reverse()
print(nger)
