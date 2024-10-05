from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        X = Counter(s1)
        fl=1
        for i in range(len(s2)-len(s1)+1):
            y = Counter(s2[i:i+len(s1)])
            fl=1
            for m in X.keys():
                if X[m]!=y[m]:
                    fl=0
                    break
            if fl!=0:
                return True
        return False
                