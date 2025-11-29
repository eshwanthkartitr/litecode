class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        t = sum(nums)
        tmp = (t//k)*k
        return t -  tmp