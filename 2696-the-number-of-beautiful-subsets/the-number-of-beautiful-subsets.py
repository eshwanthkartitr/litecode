class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i,mp):
            if i == len(nums):
                return 1
            res=dfs(i+1,mp)
            if not mp[nums[i]-k] and not mp[nums[i]+k]:
                mp[nums[i]] += 1
                res+=dfs(i+1,mp)
                mp[nums[i]]-=1
            return res 
        return dfs(0,defaultdict(int)) - 1
