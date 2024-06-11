class Solution:
    def isHappy(self, n: int) -> bool:
        l=list(map(int, str(n)))
        m=0
        while l!=[1]:
            tmp=0
            for i in l:
                tmp += i**2
            l=list(map(int, str(tmp)))
            m+=1
            print(l)
            if l!=1 and m > 7:
                return False
        return True
