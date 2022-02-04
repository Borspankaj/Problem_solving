import math
def solve_Bustation(a):
    #-----For Commulative Sum-------

    cs=set()
    s=0
    for i in a:
        s+=i
        cs.add(s)  
  
    #-------For Factors ------------
    factors=[]
    i=1
    while i<=math.sqrt(s):
        
        if s%i==0:
            if i*i==s:
                factors.append(i)
                
            else:
                factors.append(i)
                factors.append(s//i)
                
        i+=1
    
    #--------Main Code -------------
    ans=[]
    for x in sorted(factors):
        temp=x
        flag=1
        while x<=s:
            if x not in cs:
                flag=0
                break
            x+=temp
        if flag==1:
            ans.append(temp)
    return ans

