s=""
stack=[]
Q=int(input())

for _ in range(Q):
    q=input().split()
    if q[0]=='1':
        stack.append(q)
        s+=q[1]
        
    elif q[0]=='2':
        val=int(q.pop())
        q.append(s[len(s)-val:])
        stack.append(q)
        s=s[:len(s)-val]
        
        
    elif q[0]=='3':
        print(s[int(q[1])-1])
        
    else:
        last=stack.pop()
        if last[0]=='1':
            val=len(last[1])
            s=s[:len(s)-val]
            
        else:
            s+=last[1]