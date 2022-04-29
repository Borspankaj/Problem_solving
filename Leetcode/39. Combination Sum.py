class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []
        idx = 0
        def backtrack(temp,idx,arr,s):
            if s == 0:
                ans.append(temp[:])
                return 
            if s < 0 or idx == len(arr):
                return
            temp.append(arr[idx])
            backtrack(temp,idx,arr,s-arr[idx])
            temp.pop()
            backtrack(temp,idx+1,arr,s)
            
        backtrack([],idx,candidates,target)
        return ans