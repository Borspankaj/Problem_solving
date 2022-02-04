stack=[]
Q=int(input())
stack.append("")
for _ in range(Q):
    q=input().split()
    if q[0]=='1':
        s=stack[-1]+q[1]
        stack.append(s)
    elif q[0]=='2':
        s=stack[-1][:-int(q[1])]
        stack.append(s)
    elif q[0]=='3':
        print(stack[-1][int(q[1])-1])
    else:
        stack.pop()