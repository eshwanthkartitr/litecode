class Solution:
    def strangePrinter(self, s: str) -> int:
        dp={}
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == j:
                return 1
            min_val = float('inf')
            for k in range(i,j):
                min_val = min(min_val,solve(i,k)+solve(k+1,j))
            if s[i]==s[j]:
                dp[(i,j)] = min_val-1
            else:
                dp[(i,j)] = min_val
            return dp[(i,j)]
        return solve(0,len(s)-1)