class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem={0:-1}
        su=0
        for i,num in enumerate(nums):
            su += num
            if su % k in rem: 
                if i - rem[su%k] >=2:
                    return True
            else:
                rem[su%k]=i
        return False
