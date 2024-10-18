class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        re=[]
        subset=[]
        def backtrack(i):
            if len(nums)==i:
                tmp = 0
                for i in subset.copy():
                    tmp = tmp | i 
                re.append(tmp)
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return re.count(max(re))

            

