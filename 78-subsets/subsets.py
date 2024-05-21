class Solution:
    def recur(self,s):
        if len(s) == 0:
            return [[]]
        x = self.recur(s[:-1])
        return x + [[s[-1]]+y for y in x]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.recur(nums)