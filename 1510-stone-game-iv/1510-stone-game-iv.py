class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        def helper(i):
            if i == n:
                return False
            hi = False
            for j in range(1,n):
                if i+j*j>n:
                    break
                if not helper(i+j*j):
                    hi=True
            return hi
        return helper(0)