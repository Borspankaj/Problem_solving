def kthGrammar(self, n: int, k: int) -> int:
        if n==1 or k==1:
            return 0
        l=2**(n-1)
        mid=l//2
        
        if k<=mid:
            return self.kthGrammar(n-1,k)
        
        else:
            return int(not self.kthGrammar(n-1,k-mid))