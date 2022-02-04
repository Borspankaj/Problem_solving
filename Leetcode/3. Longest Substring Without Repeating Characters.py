class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0       
        for i in range(len(s)):
            chars=set()
            chars.add(s[i])
            j=i+1
            while j<len(s):
                if s[j] not in chars:
                    chars.add(s[j])
                    j+=1
                else:
                    break
            maxx=max(maxx,j-i)
        
        return maxx