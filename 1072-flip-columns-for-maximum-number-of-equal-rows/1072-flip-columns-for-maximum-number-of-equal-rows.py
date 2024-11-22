class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        re=defaultdict(int)
        for i in matrix:
            tmp = "".join([str(j) for j in i])
            inv_tmp = "".join([str(1-j) for j in i])
            key = min(tmp,inv_tmp)
            re[key]+=1  
        return max(re.values())