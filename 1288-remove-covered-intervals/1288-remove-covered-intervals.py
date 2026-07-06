class Solution:
    def removeCoveredIntervals(self, intv: List[List[int]]) -> int:
        intv.sort(key=lambda x:(x[0],-x[1]))
        cnt = 0
        max_num = 0
        for i,j in intv:
            if j > max_num:
                cnt +=1
                max_num = j
        
        return cnt