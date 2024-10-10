class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        fast = len(nums)-1
        while fast>0:
            for i in range(fast):
                if nums[i]<=nums[fast]:
                    return fast-i
            fast-=1
        return 0