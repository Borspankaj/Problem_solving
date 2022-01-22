import math

def solve_Prime(n):
    prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

    val=1
    i=0
    while True:
        val*=prime[i]
        if val>n:
            return i
        i+=1




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











