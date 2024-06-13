class Solution:
    def addDigits(self, num: int) -> int:
        q=list(str(num))
        
        while len(q) != 1:
            cnt = 0
            for i in q:
                cnt+=int(i)
            q=list(str(cnt))
        return int(q[0])
