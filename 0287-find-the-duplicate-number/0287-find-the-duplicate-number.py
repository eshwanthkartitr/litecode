class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=0
            else:
                return i
                break
        return -1