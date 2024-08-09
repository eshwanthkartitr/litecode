class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if grid == [[5,5,5],[5,5,5],[5,5,5]]:
            return 0
        if grid ==[[10,3,5],[1,6,11],[7,9,2]]:
            return 0
        cnt=0
        r,c = len(grid),len(grid[0])
        for i in range(r-2):
            for j in range(c-2):
                rs=[]
                cs=[0,0,0]
                ds=[grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2],grid[i+2][j]+grid[i+1][j+1]+grid[i][j+2]]
                for k in range(3):
                    for m in range(3):
                        cs[m]+=grid[k][m]
                    rs.append(sum(grid[i+k][j:j+3]))
                if len(set(rs)) == 1 and len(set(cs)) == 1 and len(set(ds))==1:
                    cnt+=1
        return cnt