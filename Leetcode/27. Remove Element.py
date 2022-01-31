class Solution:
    def removeElement(self, nums, val) -> int:
        p=count=0
        for i in range(len(nums)):
            if val==nums[p]:
                nums.remove(val)
                nums.append('_')
                count+=1
            else:
                p+=1
        return len(nums)-count