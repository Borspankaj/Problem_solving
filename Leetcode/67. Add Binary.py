def todeci(self,a):
    p=deci=0
    for i  in range(len(a)-1,-1,-1):
        deci=deci+(int(a[i])*(2**p))
        p+=1

    return deci
    
def tobinary(self,a):

    if a<1:
        return 0

    return str(self.tobinary(a//2)) + str(a%2)


def addBinary(self, a: str, b: str) -> str:
        
    ans1=self.todeci(a)
    ans2=self.todeci(b)

    return str(int(self.tobinary(ans1+ans2)))