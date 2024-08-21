class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def solve(i,j):
            if i == j:
                return 1
            min_val = float('inf')
            for k in range(i,j):
                min_val = min(min_val,solve(i,k)+solve(k+1,j))
            if s[i]==s[j]:
                return min_val-1
            return min_val
        return solve(0,len(s)-1)