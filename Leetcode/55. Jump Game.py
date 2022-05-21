class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        cmax = 0

        for i in range(len(nums)):
            if cmax < i:
                return False
            cmax = max(cmax , i+ nums[i])

        return True