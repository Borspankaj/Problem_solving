nums = [0,1,0,3,12]

start = -1
i = 0
if len(nums) > 1:
    while i < len(nums) :
        if nums[i] != 0 :
            start += 1

            nums[start] ,nums[i] = nums[i] , nums[start]
        i += 1
print(nums)