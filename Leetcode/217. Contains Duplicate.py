class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == len(set(nums)):
            return  False
        else:
            return True