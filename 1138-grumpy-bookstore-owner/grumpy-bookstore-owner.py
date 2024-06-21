class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        su=0
        for i in range(len(customers)):
            if grumpy[i] != 1:
                su+=customers[i]
        wind = minutes
        ma=0
        for i in range(len(customers)-wind+1):
            tmp=0
            for j in range(wind):
                if grumpy[i+j] == 1:
                    tmp+=customers[i+j]
            
            ma=max(ma,tmp)
        return ma+su