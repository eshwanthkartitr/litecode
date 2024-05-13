class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        for j in range(1, n):
            count_ones = sum(row[j] for row in grid)
            count_zeros = m - count_ones
            if count_zeros > count_ones:
                for i in range(m):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        score = 0
        for row in grid:
            binary_str = ''.join(map(str, row))
            score += int(binary_str, 2)
        
        return score