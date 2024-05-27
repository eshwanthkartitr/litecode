class Solution:
    def specialArray(self, nums: List[int]) -> int:
        res=-1
        for x in range(len(nums)+1):
            count = x
            cout=0
            for i in nums:
                if x <= i:
                    cout+=1
            if count == cout:
                return cout
        return res