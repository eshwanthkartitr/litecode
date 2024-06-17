import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            b_squared = c - i * i
            b = int(math.sqrt(b_squared))
            if b * b == b_squared:
                return True
        return False
