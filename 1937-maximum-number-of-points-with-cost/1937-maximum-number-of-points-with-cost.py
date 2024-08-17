class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        r,c = len(points),len(points[0])
        row= points[0]
        for r in range(1,r):
            ne = points[r].copy()
            left = [0] * c
            right= [0] * c
            left[0]=row[0]
            right[-1]=row[-1]
            for co in range(1,c):
                left[co]=max(row[co],left[co-1]-1)
            for i in range(c-2,-1,-1):
                right[i]=max(row[i],right[i+1]-1)
            for cunt in range(c):
                ne[cunt] += max(left[cunt],right[cunt])
            row = ne
        return max(row)