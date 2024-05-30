from collections import defaultdict
from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        letter_range = defaultdict(list)
        for i, c in enumerate(s):
            if c not in letter_range:
                letter_range[c] = [i, i]
            else:
                letter_range[c][1] = i

        for i in letter_range:
            start, end = letter_range[i]
            stack = [(start, end)]
            while stack:
                new_s, new_e = stack.pop()
                for k in range(new_s, new_e + 1):
                    hi, bye = letter_range[s[k]]
                    if hi < start:
                        stack.append((hi, start - 1))
                        start = hi
                    if bye > end:
                        stack.append((end + 1, bye))
                        end = bye
            letter_range[i] = (start, end)

        sorted_range = sorted(letter_range.values(), key=lambda x: x[1] - x[0] + 1)
        r1 = []
        ans = []
        for start, end in sorted_range:
            if any(end >= i >= start or end >= j >= start for i, j in r1):
                continue
            r1.append((start, end))
            ans.append(s[start:end + 1])
        return ans