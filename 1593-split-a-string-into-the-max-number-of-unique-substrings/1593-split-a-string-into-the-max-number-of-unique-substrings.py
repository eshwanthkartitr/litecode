class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited= list()
        def backtrack(i):
            if i==len(s):
                return 0
            
            max_splits = 0
            for simp in range(i+1,len(s)+1):
                sub = s[i:simp]
                if sub not in visited:
                    visited.append(sub)
                    max_splits = max(max_splits,1+backtrack(simp))
                    visited.pop()
            return max_splits
        return backtrack(0)