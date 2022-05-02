class Solution:
    def subsets(self, nums) :
        ans = []
        n = len(nums)
        
        def backtrack(idx,nums,temp,ans,n):
            if idx == n:
                ans.append(temp[:])
                return
            
            temp.append(nums[idx])
            backtrack(idx+1,nums,temp,ans,n)
            temp.pop()
            backtrack(idx+1,nums,temp,ans,n)
        
        backtrack(0,nums,[],ans,n)
        return ans