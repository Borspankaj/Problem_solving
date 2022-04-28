class Solution:
    def searchInsert(self, nums, target) -> int:
        for i in nums:
            if target==i:
                return nums.index(i)
            elif target<i:
                return nums.index(i)
            elif target>nums[len(nums)-1]:
                return len(nums)