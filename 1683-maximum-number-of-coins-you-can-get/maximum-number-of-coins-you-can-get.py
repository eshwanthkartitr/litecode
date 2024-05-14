class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_val = 0
        n = len(piles)
        for i in range(n // 3):
            max_val += piles[-(2 * (i+1))]
        return max_val
