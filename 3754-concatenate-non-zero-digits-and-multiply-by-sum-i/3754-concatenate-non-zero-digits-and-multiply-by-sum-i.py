class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        cnt = 0
        tmp = ""
        for i in str(n):
            if i != "0":
                tmp+=i
            cnt+=int(i)
        return int(tmp)*cnt
        
