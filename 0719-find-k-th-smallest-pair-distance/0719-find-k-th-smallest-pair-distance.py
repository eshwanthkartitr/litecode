class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def hi(val):
            l =0
            re=0
            for i in range(len(nums)):
                while nums[i]-nums[l]>val:
                    l+=1
                re+=i-l
            return re
        l=0
        r=max(nums)
        while l<r:
            m=l+((r-l)//2)
            pairs=hi(m)
            if pairs>=k:
                r=m
            else:
                l=m+1
        return l