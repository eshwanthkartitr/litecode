class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        x=sorted([x for x in nums],key = lambda x:nums.count(x),reverse=True)
        x.reverse()
        return x