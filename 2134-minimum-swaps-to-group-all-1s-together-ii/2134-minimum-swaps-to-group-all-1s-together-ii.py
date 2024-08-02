class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt = nums.count(1)
        nums.extend(nums)
        re = float('inf')
        for i in range(len(nums)):
            if len(nums[i:i+cnt]) < cnt:
                break
            tmp = [1]*cnt
            hi = nums[i:i+cnt].count(0)
            print(nums[i:i+cnt])
            if hi == 0:
                return 0
            re = min(re,hi)
        return re