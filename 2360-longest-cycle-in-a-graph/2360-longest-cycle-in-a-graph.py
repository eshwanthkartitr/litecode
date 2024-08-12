class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        longest = -1
        
        for head in range(n):
            slow = head
            fast = head
            
            while edges[fast] != -1 and edges[edges[fast]] != -1:
                slow = edges[slow]
                fast = edges[edges[fast]]
                
                if slow == fast:
                    cycle_length = 1
                    fast = edges[fast]
                    while fast != slow:
                        fast = edges[fast]
                        cycle_length += 1
                    
                    longest = max(longest, cycle_length)
                    while edges[head] != -1:
                        next_node = edges[head]
                        edges[head] = -1
                        head = next_node
                    
                    break 
        
        return longest
