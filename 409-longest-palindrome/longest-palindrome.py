class Solution:
    def longestPalindrome(self, s: str) -> int:
        hlo = Counter(s)
        result=0
        ex=False
        for i in hlo.keys():
            if hlo[i] % 2 == 0:
                result += hlo[i]
            elif hlo[i] != 1:
                result += (hlo[i]//2)*2
                ex=True
            else:
                ex = True
        if ex == True:
            return result+1
        else:
            return result
