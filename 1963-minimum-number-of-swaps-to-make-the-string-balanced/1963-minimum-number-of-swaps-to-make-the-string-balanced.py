class Solution:
    def minSwaps(self, s: str) -> int:
        max_num=0
        num=0
        for i in s:
            if i==']':
                num+=1
            else:
                num-=1
            max_num=max(max_num,num)
        return (max_num+1)//2