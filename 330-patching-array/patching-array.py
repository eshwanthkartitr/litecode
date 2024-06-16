class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        #chng=nums
        #li=[i for i in range(n)]
        #re=set()
        #subset=[]
        #def backtrack(i):
        #    if i>=len(chng):
        #        re.add(sum(subset))
        #        return
        #    subset.append(chng[i])
        #    backtrack(i+1)
        #    subset.remove(chng[i])
        #    backtrack(i+1)
        #cnt=0
        #while True:
        #    re.clear()
        #    backtrack(0)
        #    missing=-1
        #    for i in li:
        #        if i not in re:
        #            missing=i
        #            break
        #    if missing == -1:
        #        break
        #    chng.append(missing)
        #    cnt+=1
        #return cnt
        patches = 0
        miss = 1
        i = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        
        return patches
        