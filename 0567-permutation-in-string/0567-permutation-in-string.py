from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        X = Counter(s1)
        fl=1
        y = Counter(s2[:len(s1)])
        if X==y:
            return True
        for i in range(1,len(s2)-len(s1)+1):
            y[s2[i-1]]-=1
            y[s2[i+len(s1)-1]]+=1
            if X==y:
                return True
        return False
                