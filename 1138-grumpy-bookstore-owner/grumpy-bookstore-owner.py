class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        right = minutes - 1
        candidate = 0
        for i in range(len(customers)):
            candidate += customers[i]*abs(grumpy[i] - 1)
        for i in range(left, right+1):
            candidate += customers[i]*grumpy[i]
        ans = candidate
        while right < len(customers) - 1:
            candidate += customers[right+1]*grumpy[right+1]
            candidate -= customers[left]*grumpy[left]
            if candidate > ans:
                ans = candidate
            left += 1
            right += 1
        return ans