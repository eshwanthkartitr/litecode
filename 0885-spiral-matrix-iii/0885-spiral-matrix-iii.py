class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        p_dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        re = []
        steps=1
        i=0
        r,c = rStart,cStart
        while len(re) < rows*cols:
            for _ in range(2):
                cr,cc = p_dir[i]
                for _ in range(steps):
                    if (0<=r<rows) and (0<=c<cols):
                        re.append([r,c])
                    r,c = cr+r,cc+c
                i = (i+1)%4
            steps+=1 
        return re