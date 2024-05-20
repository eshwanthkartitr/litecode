class Solution:
    def recur(self,s):
        if len(s) == 0:
            return [[]]
        x = self.recur(s[:-1])
        return x+[[s[-1]] + y for y in x]
    def subsetXORSum(self, nums: List[int]) -> int:
        result = self.recur(nums)
        total=0
        for i in result:
            temp=0
            for j in i:
                temp^=j
            total+=temp
        return total
