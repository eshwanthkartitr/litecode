class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        n = sorted(heights)
        for i in range(len(heights)):
            if n[i] != heights[i]:
                count+=1
        return count 