def solve(nums,k):
    n=len(nums)
    s=0
    for i in range(k):
        s+=nums[i]
        print(s)
    maxx=s
    start=0
    end=i+1
    while end<n:
        s=s-nums[start]+nums[end]
        maxx=max(maxx,s)
        start+=1
        end+=1

    return maxx/k

solve([1,12,-5,-6,50,3],4)


