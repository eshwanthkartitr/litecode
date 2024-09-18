class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        re=[]
        for i in nums:
            re.append(str(i))
        my = sorted(re,key=lambda x:x*2)[::-1]
        print(my[::-1])
        return "".join(my) 