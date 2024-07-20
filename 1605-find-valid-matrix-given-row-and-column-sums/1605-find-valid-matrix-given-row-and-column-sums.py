class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r_l = len(rowSum)
        c_l = len(colSum)
        re=[[0]*c_l for _ in range(r_l)]
        for j in range(c_l):
            for i in range(r_l):
                re[i][j] = min(rowSum[i],colSum[j])
                rowSum[i]-=re[i][j]
                colSum[j]-=re[i][j]
        return re

        