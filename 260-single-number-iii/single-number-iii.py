class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        re=[]
        for i in nums:
            if nums.count(i) == 1:
                re.append(i)
        return re
        