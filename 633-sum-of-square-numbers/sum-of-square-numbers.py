import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c))+1):
            b=c-(i*i)
            if int(math.sqrt(b))*int(math.sqrt(b)) == b:
                return True
        return False
