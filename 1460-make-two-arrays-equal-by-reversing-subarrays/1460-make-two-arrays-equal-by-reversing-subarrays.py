class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in arr:
            n1 = target.count(i)
            n2 = arr.count(i)
            if  n1!=n2:
                return False
        return True