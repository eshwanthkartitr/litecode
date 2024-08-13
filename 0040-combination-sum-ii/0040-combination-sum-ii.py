class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        re=[]
        subset=[]
        def backtrack(target,i):
            if target<0:
                return
            if target == 0:
                if subset.copy() not in re:
                    re.append(subset.copy())
                return
            if i>=len(candidates):
                return 
            subset.append(candidates[i])
            backtrack(target-candidates[i],i+1)
            subset.remove(candidates[i])
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(target,i+1)
        backtrack(target,0)
        return re