class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        re=[]
        for i in arr2:
            for _ in range(arr1.count(i)):
                re.append(i)
        arr1.sort()
        for i in arr1:
            if i not in re:
                for _ in range(arr1.count(i)):
                    re.append(i)

        return re
            