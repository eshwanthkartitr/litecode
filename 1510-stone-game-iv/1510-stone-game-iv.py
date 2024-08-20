class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def helper(i):
            if i == 0:
                return False
            for j in range(1,int(i**0.5)+1):
                if i-j*j<0:
                    break
                if not helper(i-j*j):
                    return True
            return False
        return helper(n)