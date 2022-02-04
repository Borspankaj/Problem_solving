def superReducedString(s):
    
    l=len(s)
    stack=[]
    for i in s:
        if not stack:
            stack.append(i)

        else:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
    ans="".join(stack)      
    if ans=="":
        return 0
    else:
        return ans
