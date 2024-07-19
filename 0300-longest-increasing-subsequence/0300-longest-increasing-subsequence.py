class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1  for _ in range(len(nums))]
        i=1
        while i != len(nums):
            j=0
            while j!=i+1:
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
                j+=1
            i+=1
        print(dp)
        return max(dp)