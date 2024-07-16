class Solution:
    def convertToTitle(self, x: int) -> str:
        if x <= 26:
            return chr(ord('A')+x-1)
        hi=[]
        while x > 0:
            x-=1
            hi.append(chr(ord('A')+x%26))
            x = x// 26
        return "".join(hi[::-1])