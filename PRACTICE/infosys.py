import math
import sys

def isPrime(n):
    if n <= 1 :
        return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
 

def F(n):
    k=[]
    for e in n:
        count=0
        for i in range(2, n + 1):
            if isPrime(i):
                count+=1
        k.append(count)
    return k


def solve(n,q,a,t,l,r):
    ans=[]
    for i in range(n):
        if t[i]==1:
            ans.append(sum(a[l:r+1]))
        else:
            ans+=F(a[l:r+1])
    return sum(ans)


    







