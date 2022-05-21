class Solution:
    def missingNumber(self, nums) :
        freq = [False]*(max(nums)+1)
        
        for i in nums :
            freq[i] = True
            
        for i in range(len(nums)):
            if not freq[i]:
                return i
        return len(nums)    
        