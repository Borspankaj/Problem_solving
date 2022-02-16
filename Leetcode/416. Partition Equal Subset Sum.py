class Solution:
    def canPartition(self, nums) -> bool:
        s=sum(nums)
    
        if s%2!=0:
            return False
        s//=2
        dp=[[0]* (s+1) for i in range(len(nums)+1)]
        for i in range(s+1):
            dp[0][i]=False
        for i in range(len(dp)):
            dp[i][0]=True

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if nums[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]




        return dp[-1][-1]
        