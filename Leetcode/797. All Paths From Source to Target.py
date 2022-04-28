class Solution:
    def allPathsSourceTarget(self, graph):
        def backtrack(ind,target,graph,temp,ans):
            if ind==target:
                ans.append(temp[:])
                return
            
            if graph[ind]==[]:
                return
            for v in graph[ind]:
                temp.append(v)
            
                backtrack(v,target,graph,temp,ans)
                temp.pop()
            return ans   
        ans=backtrack(0,len(graph)-1,graph,[0],[])
        return ans