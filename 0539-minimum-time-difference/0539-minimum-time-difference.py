class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        re=[]
        for i in timePoints:
            re.append(int(i[:2])*60+int(i[3:]))
        re.sort()
        diff=[]
        for i in range(1,len(re)):
            diff.append(re[i]-re[i-1])
        print(re)
        return min(min(diff),24*60 - re[-1] + re[0])