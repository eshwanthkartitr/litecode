class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr=[1]
        for i in range(n-1):
            val = min(arr)
            arr.remove(val)
            for j in [2,3,5]:
                if val*j not in arr:
                    arr.append(val*j)
        return min(arr) 