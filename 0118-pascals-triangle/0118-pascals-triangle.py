class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tmp = []
        if numRows >= 1:
            tmp.append([1])
        if numRows >=2:
            tmp.append([1,1])
        
        for i in range(numRows-2):
            li = tmp[-1]
            row = [1] +[li[m] + li[m+1] for m in range(len(li)-1)] + [1]
            tmp.append(row)
        return tmp
                