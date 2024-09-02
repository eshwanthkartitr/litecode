class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        while k>=0:
            k=k-chalk[i]
            i=(i+1)%len(chalk)
        return i-1
