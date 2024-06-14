class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] <= 0:
                cnt+=nums[i-1]-nums[i]+1
                nums[i]=nums[i-1]+1
        return cnt