import numpy as np

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(i, j, visited, tmp):
            if (i, j) in visited or tmp[i][j] == 0:
                return
            visited.add((i, j))
            tmp[i][j] = 0
            if i + 1 < len(grid):
                dfs(i + 1, j, visited, tmp)
            if j - 1 >= 0:
                dfs(i, j - 1, visited, tmp)
            if i - 1 >= 0:
                dfs(i - 1, j, visited, tmp)
            if j + 1 < len(grid[0]):
                dfs(i, j + 1, visited, tmp)
            return
        hi = np.array(grid).flatten()
        if 1 not in hi:
            return 0
        def cnt_reg(tmp):
            regions=0
            vist=set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if tmp[i][j]!=0 and (i,j) not in vist:
                        dfs(i,j,vist,tmp)
                        tmp[i][j]=0
                        regions+=1
            return regions
        if cnt_reg([row[:] for row in grid])!=1:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    tmp = [row[:] for row in grid]
                    tmp[i][j] = 0
                    if cnt_reg(tmp) != 1:
                        return 1
        return 2