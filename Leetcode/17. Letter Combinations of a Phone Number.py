class Solution:
    def letterCombinations(self, digits: str):
        def backtrack(temp,hmap,ans,idx,digits):
            if idx==len(digits):
                ans.append("".join(temp[:]))
                return 

            for i in hmap[digits[idx]]:
                temp.append(i)
                backtrack(temp,hmap,ans,idx+1,digits)
                temp.pop()
        hmap={'2':list('abc'),'3':list('def'),'4':list('ghi'),'5':list('jkl'),'6':list('mno'),'7':list('pqrs'),'8':list('tuv'),'9':list('wxyz')}
        ans=[]
        temp=[]
        backtrack(temp,hmap,ans,0,digits)
        if ans[0]=="": return []
        else: return ans 


        
