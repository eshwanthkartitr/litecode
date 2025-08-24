class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """ After a long fucking day"""
        n = len(nums)
        if 0 not in nums:
            return n-1
        # tip = 0
        # for i in range(n):
        #     tmp = 0
        #     cnt = 0
        #     for no in nums[:i] + nums[i+1:]:
        #         if(no==1):
        #             cnt+=1
        #         else:
        #             cnt =0
        #         tmp = max(tmp,cnt)
        #     tip = max(tip,tmp)
        # return tip
        dp = []
        cnt =0
        for i in range(n):
            if(nums[i]==1):
                cnt+=1
            else:
                dp.append(cnt)
                cnt = 0
        dp.append(cnt)
        cnt = 0
        n =len(dp)
        for i in range(n-1):
            cnt = max(cnt,dp[i]+dp[i+1])
        return cnt

