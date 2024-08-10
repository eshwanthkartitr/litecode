class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        p1,p2 = len(grid),len(grid[0])
        p3,p4 = 3*p1,3*p2
        t=[[0]*p4 for _ in range(p3)]
        for i  in range(p1):
            for j in range(p2):
                a1,a2=3*i,j*3
                if grid[i][j]=="/":
                    t[a1][a2+2]=1
                    t[a1+1][a2+1]=1
                    t[a1+2][a2]=1
                if grid[i][j]=="\\":
                    t[a1][a2]=1
                    t[a1+1][a2+1]=1
                    t[a1+2][a2+2]=1
        regions=0
        def dfs(i,j,visited):
            if (i,j) in visited or t[i][j]!=0:
                return 
            visited.add((i,j))
            t[i][j]=1
            if 0<=j+1<len(t[0]):
                print(i,j)
                dfs(i,j+1,visited)
            if 0<=j-1<len(t[0]): 
                dfs(i,j-1,visited)
            if 0<=i-1<len(t):
                dfs(i-1,j,visited)
            if 0<=i+1<len(t):
                dfs(i+1,j,visited)
        visited=set()
        for i in range(p3):
            for j in range(p4):
                if t[i][j]!=1:
                    dfs(i,j,visited)
                    regions+=1
        return regions
        
                        
