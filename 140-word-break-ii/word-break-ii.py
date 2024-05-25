class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        re=[]
        cur=[]
        def backtrack(i):
            if i >=len(s):
                re.append(" ".join(cur))
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return re