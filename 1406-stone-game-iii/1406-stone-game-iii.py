class Solution:
    def stoneGameIII(self, k: List[int]) -> str:
        @cache
        def helper(i):
            if i==len(k):
                return 0
            total = -float('inf')
            for j in range(1,4):
                if i+j>len(k):
                    break
                total = max(total,sum(k[i:i+j])-helper(i+j))
            return total
        tmp = helper(0)
        if tmp==0:
            return "Tie"
        if tmp>0:
            return "Alice"
        else:
            return "Bob"
