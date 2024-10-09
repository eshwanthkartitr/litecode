class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s=="()":
            return 0
        ss=[]
        for i in range(len(s)):
            if len(ss) >= 2 and ss[-2]=="(" and ss[-1]==")":
                ss.pop()
                ss.pop()
            ss.append(s[i]) 
        return len(ss)