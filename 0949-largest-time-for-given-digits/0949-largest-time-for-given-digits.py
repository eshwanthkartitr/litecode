from itertools import permutations 
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        return max([f"{H}{h}:{M}{m}" for H, h, M, m in permutations(A) if H*10 + h < 24 and M < 6], default="")