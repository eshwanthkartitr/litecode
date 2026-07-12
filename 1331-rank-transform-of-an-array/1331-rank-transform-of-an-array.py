class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tmp = {rank:val for val, rank in enumerate(sorted(set(arr)),1)}
        return [tmp[x] for x in arr]