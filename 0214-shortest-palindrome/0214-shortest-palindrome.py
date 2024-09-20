class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """if list(s)==list(s)[::-1]:
            return s
        else:
            s=list(s)
            prefix=[]
            suffix=[]
            for i in range(len(s)):
                prefix.append(s[:i])
            rev=s[::-1]
            for i in range(len(s)):
                suffix.append(rev[-i:len(s)])
            longest=[i for i in prefix if i in suffix]
            maximum = len(longest[-1])
            return "".join(s[maximum:][::-1]) + "".join(s)"""
        if s == s[::-1]:
            return s
        rev = s[::-1]
        for i in range(len(s)):
            if s.startswith(rev[i:]):
                return rev[:i] + s
        return ""
