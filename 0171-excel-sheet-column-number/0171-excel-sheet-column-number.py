class Solution:
    def titleToNumber(self, x: str) -> int:
        x=list(x)[::-1]
        cnt=0
        for i in range(len(x)):
            cnt+=(ord(x[i])-ord('A')+1)*26**i
        return cnt