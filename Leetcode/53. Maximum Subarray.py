class Solution:
    def maxSubArray(self, a) -> int:
        maxx=max_sum=a[0]
        for i in range(1,len(a)):
            maxx=max(a[i],maxx+a[i])
            max_sum=max(maxx,max_sum)
        return max_sum