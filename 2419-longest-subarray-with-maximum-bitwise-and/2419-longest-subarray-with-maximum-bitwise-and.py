class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num=max(nums)
        streak=0
        ma=1
        for i in range(len(nums)):
            if nums[i]==max_num:
                streak+=1
            else:
                streak=0
            ma=max(ma,streak)
        return ma