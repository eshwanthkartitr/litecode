class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        x=sorted(nums,key = lambda x:nums.count(x),reverse=True)
        return x[::-1]