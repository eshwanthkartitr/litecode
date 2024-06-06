from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])

        max_product = max(dp[i][0] for i in range(n))
        return max_product
