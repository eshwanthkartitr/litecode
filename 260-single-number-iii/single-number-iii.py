class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        re=0
        for i in nums:
            re^=i        
        diff=1
        while not(re & diff):
            diff <<=1
        a,b=0,0
        for i in nums:
            if diff & i:
                a = a^i
            else:
                b=b^i
        return [a,b]