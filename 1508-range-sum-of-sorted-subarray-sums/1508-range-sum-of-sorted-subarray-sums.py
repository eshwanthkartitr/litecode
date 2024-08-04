class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        re=[]
        for window in range(n):
            su=0
            for j in range(window,n):
                su +=nums[j]
                re.append(su)
        re.sort()
        ans = 0
        for j in range(left-1,right):
            ans+=re[j]
        return ans%(10**9+7)