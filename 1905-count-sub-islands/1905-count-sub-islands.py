class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        @cache
        def helper(i,j):
            if i<0 or i>=len(grid2) or j<0 or j>=len(grid2[0]):
                return True
            is_sub=True
            if grid2[i][j] == 0:
                return True
            if grid1[i][j] == 0:
                return False
            grid2[i][j] = 0
            is_sub&=helper(i+1,j)
            is_sub&=helper(i,j-1)
            is_sub&=helper(i,j+1)
            is_sub&=helper(i-1,j)
            return is_sub
        cnt=0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]==1:
                    if helper(i,j):
                        cnt+=1
        return cnt