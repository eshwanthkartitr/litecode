class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sum1 = 0
        var2=0
        var1=float("inf")
        for i in nums:
            if(i^k > i):
                sum1 += i^k
                var1 = min(var1,(i^k)-i)
                var2+=1
            else:
                sum1 += i
                var1 = min(var1,i-(i^k))
        if (var2%2== 0):
            return sum1
        else:
            return sum1-var1