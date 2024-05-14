class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0

        def dfs(i, j, cur_gold, visited):
            nonlocal max_gold
            if 0 <= i < m and 0 <= j < n and grid[i][j] != 0 and (i, j) not in visited:
                visited.add((i, j))
                cur_gold += grid[i][j]
                max_gold = max(max_gold, cur_gold)

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(i + dx, j + dy, cur_gold, visited)

                visited.remove((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0, set())

        return max_gold