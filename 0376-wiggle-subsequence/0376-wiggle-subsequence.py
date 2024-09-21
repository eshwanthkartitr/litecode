class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cnt=1 
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if cnt==1 or (nums[i]-nums[i-1])*(nums[i-1]-nums[i-2]) < 0:
                    cnt+=1
        return cnt