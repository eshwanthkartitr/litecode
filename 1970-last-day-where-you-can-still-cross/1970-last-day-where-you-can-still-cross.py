class Solution:
    def canCross(self, day, row, col, cells):
        m, n = row, col
        dp = [[-1]*n for _ in range(m)]
        for i in range(day):
            x, y = cells[i]
            dp[x-1][y-1] = 1

        from collections import deque
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        visited = [[False]*n for _ in range(m)]
        for j in range(n):
            if dp[0][j] == -1:
                q.append((0, j))
                visited[0][j] = True

        while q:
            x, y = q.popleft()
            if x == m-1:
                return True
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and dp[nx][ny] == -1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        lo, hi = 1, len(cells)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canCross(mid, row, col, cells):
                ans = mid          
                lo = mid + 1
            else:
                hi = mid - 1       
        return ans
