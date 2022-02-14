class Solution:
    def climbStairs(self, n: int) -> int:
        l=[1,2]
        if n<3:
            return l[n-1]
        for i in range(2,n):
            val=l[i-1]+l[i-2]
            l.append(val)
        return l[-1]