
def solve(nums,k):
    n=len(nums)
    start=end=0
    vals=set()

    if n==1:
        return False
    while end<n:
        if end<=k:
            if nums[end] in vals:
                return True
            else:
                vals.add(nums[end])
        else:
            vals.remove(nums[start])
            if nums[end] in vals:
                return True
            else:
                vals.add(nums[end])
            start+=1
        end+=1
    return False


print(solve([99,99],2))
    




