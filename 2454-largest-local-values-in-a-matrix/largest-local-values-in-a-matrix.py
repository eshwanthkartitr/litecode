class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        arr=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                for k in range(3):
                    arr[i][j] = max(arr[i][j],max(grid[i+k][j:j+3]))
        return arr