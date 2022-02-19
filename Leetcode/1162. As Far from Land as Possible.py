class Solution:
    def maxDistance(self, grid) -> int:
            q=[]
            water=land=0
            n=len(grid)
            indices=[(0,1),(0,-1),(1,0),(-1,0)]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        land+=1
                        q.append((0,(i,j)))
                    if grid[i][j]==0:
                        water+=1
            if water==0 or land==0:
                return -1

            while q:

                step,cell=q.pop(0)

                i,j=cell
                for id1,id2 in indices:
                    newi=i+id1
                    newj=j+id2

                    if 0<=newi<n and 0<=newj<n and grid[newi][newj]==0:
                        grid[newi][newj]=1
                        q.append((step+1,(newi,newj)))


            return step         
# grid = [[1,0,1],[0,0,0],[1,0,1]]
# print(maxDistance(grid))