class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = sum(nums)
        delta=[]
        for i in nums:
            delta.append((i^k) -i)
        print(delta)
        delta.sort(reverse=True)
        print(delta)
        
        for i in range(0,len(delta),2):
            if i+1>=len(delta):
                break
            if delta[i]+delta[i+1] > 0:
                total+=delta[i]+delta[i+1]
        return total
