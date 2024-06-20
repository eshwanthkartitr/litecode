class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()  # Sort the positions to use binary search
        n = len(position)
        
        def can_place(distance):
            count = 1  # Start with the first element placed
            last_position = position[0]
            
            for i in range(1, n):
                if position[i] - last_position >= distance:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        lo = 0
        hi = position[-1] - position[0] + 1
        best_distance = 0
        
        while lo <= hi:
            mid = (lo + hi) >> 1
            if can_place(mid):
                best_distance = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return best_distance