class Solution:
    def permute(self, nums) :
        
        def backtrack(nums,left,right,ans):
            if left==right:
                ans.append(nums[:])
                return
            
            for i in range(left,right+1):
                nums[i],nums[left]=nums[left],nums[i]
                backtrack(nums,left+1,right,ans)
                nums[i],nums[left]=nums[left],nums[i]
                
        ans=[]
        backtrack(nums,0,len(nums)-1,ans)
        return ans