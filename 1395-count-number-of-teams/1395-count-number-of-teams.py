class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt=0
        for i in range(1,len(rating)-1):
            left_small = right_large=0
            for j in range(i):
                if rating[j]<rating[i]:
                    left_small+=1
            for k in range(i+1,len(rating)):
                if rating[i]<rating[k]:
                    right_large+=1 
            cnt+=left_small*right_large
            left_large = i-left_small
            right_small = len(rating)-i-1-right_large
            cnt+=left_large*right_small
        return cnt
        