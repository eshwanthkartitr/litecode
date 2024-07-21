#Day -1 of copying shit
from typing import *
from collections import defaultdict

class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[ List[ int ] ],
        colConditions: List[ List[ int ] ]
        ) -> List[ List[ int ] ]:
        
        rowOrder = Solution().sort_conditions( rowConditions, k )
        if not rowOrder: return []
        
        colOrder = Solution().sort_conditions( colConditions, k )
        if not colOrder: return []
        
        row_position = [0] * (k+1)
        col_position = [0] * (k+1)
        for row_col, (row_value, col_value) in enumerate(zip(rowOrder, colOrder)):
            row_position[ row_value ] = row_col
            col_position[ col_value ] = row_col
            
        result = [ [0] * k for _ in range(k) ]
        
        for value in range(1,k+1):
            result[ row_position[value] ][ col_position[ value ] ] = value
        
        return result
    
    def sort_conditions(
        self,
        conditions,
        k
        ):
        
        must_be_after = defaultdict(set)
        
        for [before_i, after_i] in conditions:
            
            must_be_after[ after_i ].add( before_i )
            
        current_order = []
        set_already_placed = set()
        not_stuck = True
        
        while not_stuck:
            not_stuck = False
            for i in range(1, k+1):
                if (
                    i not in set_already_placed and
                    must_be_after[ i ].issubset( set_already_placed )
                ):
                    current_order.append(i)
                    set_already_placed.add( i )
                    not_stuck = True
                    
        if set( range(1, k+1 ) ).issubset( set_already_placed ):
            return current_order
        else:
            return []