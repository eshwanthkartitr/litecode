class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        t = defaultdict(list)
        for idx,i in enumerate(nums):
            t[i].append(idx)
        
        aar = [0]*len(nums)
        for pos in t.values():
            m = len(pos)
            prefix = [0] * (m + 1)

            for i in range(m):
                prefix[i + 1] = prefix[i] + pos[i]

            for i, p in enumerate(pos):
                left = p * i - prefix[i]
                right = (prefix[m] - prefix[i + 1]) - p * (m - i - 1)
                aar[p] = left + right

        return aar