class Solution:
    def get_longest(self,s,left,right):
       
        if not s or left>right:
            return 0
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left -1
    
    def longestPalindrome(self, s: str) -> str:
        
        if not s or len(s)<1:
            return ""
        start=end=0
        
        for i in range(len(s)):
            l1=self.get_longest(s,i,i)
            l2=self.get_longest(s,i,i+1)
            
            m=max(l1,l2)
            if m>end-start:
                end=(m//2)+i
                start=i-((m-1)//2)
                
                
        return s[start:end+1]