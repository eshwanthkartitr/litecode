class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i=0
        n=len(part)
        while s and i<len(s):
            if s[i:i+n] == part:
                s = s[:i]+s[i+n:]
                i=0
            else:
                i+=1 
        return s