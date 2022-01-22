    
def solve(s,t):
    d1={}
    d2={}
    for i in range(len(s)):
        if s[i] not in d1:
            index1=i
            d1[s[i]]=i
                
        else:
            index1=d1[s[i]]

        if t[i] not in d2:
            index2=i
            d2[t[i]]=i
                
        else:
            index2=d2[t[i]]


        if index1!=index2:
            return False
    return True
    

print(solve('foo','bar'))
                