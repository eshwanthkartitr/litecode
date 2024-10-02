class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if arr==[]:
            return []
        if max(arr)==min(arr):
            return [1]*len(arr)
        else:
            order = list(set(arr))
            order = sorted(order)
            has={}
            re=[]
            for i,c in enumerate(order):
                has[c]=i
            for i in range(len(arr)):
                re.append(has[arr[i]]+1)
            return re
            
