class Solution:
    def maxProfit(self, prices) -> int:
        g=-1
        stack=[]
        for i in range(len(prices)-1,-1,-1):
            stack.append(g)
            g=max(g,prices[i])
        stack=stack[::-1]
        profit=0
        for i in range(len(prices)):
            profit=max(stack[i]-prices[i],profit)

        return profit