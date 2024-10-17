class Solution:
    def maximumSwap(self, num: int) -> int:
        if len(str(num))==1:
            return num
        s=list(str(num))
        ma=num
        for i in range(len(s)-1):
            val = max(s[i+1:])
            idx = len(s)-1-s[::-1].index(val)
            ma=max(ma,int("".join(s[:i]+[s[idx]]+s[i+1:idx]+[s[i]]+s[idx+1:])))
        return ma