# Accountability : Gpt has given this code but fuckkkkkkkkkkkkkkkkkkkkkkk a two pass greedy approach 
# so my approach involved backtracking and failed in the 7th case  
# This approach is a left pass which checks for zero char or ( why ?
# Cause we can change if locked[i] is zero but why is ( also checked the assumption is if ) comes with less than zero wherease zero gives the freedom of choice 
# Now implement this in right search but now we check for zeroth char as well as ) cause ( which does not have any ) or 0 character to it's right side 
# Fuckkkkkkkkkkkkkk this is a good question ok so i am planning on making some comments for my futureself which can make retain my mentality and think if i have grown or nahhhhhhhhhhhhhhhhhhhhh
# Top Approach: 
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n%2!=0:
            return False
        bal = 0
        for i in range(n):
            if locked[i]=="0" or s[i]=='(':
                bal+=1
            else:
                bal-=1
            if bal<0:
                return False 
        bal=0
        for i in range(n-1,-1,-1):
            if locked[i]=="0" or s[i]==')':
                bal+=1
            else:
                bal-=1
            if bal<0:
                return False
        return True