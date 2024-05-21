class Solution:
    def recur(self,s):
        if len(s) == 0:
            return [[]]
        x = self.recur(s[:-1])
        return x + [[s[-1]]+y for y in x]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #return self.recur(nums)
        re=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                re.append(subset.copy())
                return 
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return re