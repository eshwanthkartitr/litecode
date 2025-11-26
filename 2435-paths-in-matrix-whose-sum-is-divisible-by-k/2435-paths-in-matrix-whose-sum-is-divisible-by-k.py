class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        mad = 10**9 + 7 
        moves = [(1,0),(0,1)]
        tot=0
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for l in range(k):
                    if dp[i][j][l]:
                        for mo in moves:
                            dx = i+mo[0]
                            dy = j+mo[1]
                            if 0<=dx<m and 0<=dy<n:
                                madd = (l+grid[dx][dy])%k
                                dp[dx][dy][madd] = (dp[dx][dy][madd] + dp[i][j][l])%mad
        
        return dp[m-1][n-1][0]