class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if "AB" not in s and "CD" not in s:
                return len(s)
            if "AB" in s:
                s= s.replace("AB","")
            if "CD" in s:
                s= s.replace("CD","")
            