class Solution:
    def nearestExit(self, maze, entrance) -> int:
        q=[]
        indices=[(0,-1),(0,1),(-1,0),(1,0)]
        m=len(maze)
        n=len(maze[0])
        q.append((0,entrance))
        maze[entrance[0]][entrance[1]]='+'
        while q:
            step,cell=q.pop(0)
            i=cell[0]
            j=cell[1]
            if cell!=entrance:
                for ci,cj in indices:
                    if i+ci<0 or i+ci>=m or j+cj<0 or j+cj>=n:
                        return step
            for ci,cj in indices:
                if 0<=i+ci<m and 0<=j+cj<n and maze[i+ci][j+cj]=='.':
                    q.append((step+1,(i+ci,j+cj)))
                    maze[i+ci][j+cj]='+'

        return -1
        
# maze = [["+","+","+"],[".",".","."],["+","+","+"]]
# entrance = [1,0]
# print(nearestExit(maze, entrance))