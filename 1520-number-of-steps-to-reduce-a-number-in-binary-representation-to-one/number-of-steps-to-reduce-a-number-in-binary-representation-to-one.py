class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s,2)
        count = 0
        while number != 1:
            count += 1
            if number % 2 == 1:
                number += 1
            else:
                number //= 2
        return count
