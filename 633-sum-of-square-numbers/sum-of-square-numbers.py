import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c))+1):
            try:
                if i*i + int(math.sqrt(c-(i*i)))*int(math.sqrt(c-(i*i))) == c:
                    return True
            except:
                continue
        return False
