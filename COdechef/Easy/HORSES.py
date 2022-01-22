try:
    T = int(input())
    for _ in range(T):
        n = int(input())
        nums = list(map(int,input().split()))
        
        nums.sort()
        mini = nums [-1]

        for i in range(1,n):
            mini = min(mini,nums[i]-nums[i-1])

        print (mini)


except Exception as e:
    pass