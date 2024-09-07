class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        re=[]
        for i in list(set(nums)):
            re.append((i**2,i))
        re.sort() 
        if re[0][1] < 0 and re[0][0]==re[1][0]:
            return re[1][1]
        else:
            return re[0][1]