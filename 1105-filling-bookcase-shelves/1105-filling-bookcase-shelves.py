class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache
        def backtrack(i):
            nonlocal shelfWidth,books
            if len(books)==i:
                return 0
            cur_width = shelfWidth
            re=float('inf')
            max_height = 0
            for poss in range(i,len(books)):
                if cur_width - books[poss][0] >= 0:
                    cur_width -= books[poss][0]
                    max_height = max(max_height,books[poss][1])
                else:
                    break
                re = min(re,backtrack(poss+1)+max_height)
            return re
        return backtrack(0)