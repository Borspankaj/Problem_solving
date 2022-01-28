class Solution:
    def solve(self,arr,count,k,n):
        if n==1:
            return arr[0]
        count=(count+k-1)%n
        arr.pop(count)
        return self.solve(arr,count,k,n-1)
        
    def findTheWinner(self, n: int, k: int) -> int:
        arr=list(range(1,n+1))
        return self.solve(arr,0,k,n)