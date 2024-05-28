class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        curr_cost = 0
        max_lenn = 0

        while right < len(s):
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            # If the current cost exceeds maxCost, move the left pointer to reduce the window size
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_lenn = max(max_lenn, right - left + 1)
            right += 1
        
        return max_lenn
