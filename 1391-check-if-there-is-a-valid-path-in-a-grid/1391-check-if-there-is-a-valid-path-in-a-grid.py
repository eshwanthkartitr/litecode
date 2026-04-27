class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        mp={
            1:['L','R'],
            2:['U','D'],
            3:['L','D'],
            4:['D','R'],
            5:['L','U'],
            6:['U','R']
        }

        opp={
            'L':'R',
            'R':'L',
            'U':'D',
            'D':'U'
        }

        m, n = len(grid), len(grid[0])
        stack = [(0, 0)]
        visited = set([(0, 0)])

        dire = [
            (0, -1, 'L'),
            (0, 1, 'R'),
            (-1, 0, 'U'),
            (1, 0, 'D')
        ]

        while stack:
            x,y=stack.pop()
            tmp = mp[grid[x][y]]

            if x == m-1 and y==n-1:
                return True
            cur = mp[grid[x][y]]
            for dx,dy,d in dire:
                nx, ny = x + dx, y + dy
                
                if 0<=nx<m and 0<=ny<n:
                    if d in cur and opp[d] in mp[grid[nx][ny]]:
                        if (nx,ny) not in visited:
                            visited.add((nx,ny))
                            stack.append((nx,ny))
        
        return False



        

