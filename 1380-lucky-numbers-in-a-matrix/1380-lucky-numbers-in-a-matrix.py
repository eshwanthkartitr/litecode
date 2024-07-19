class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_ele = []
        for i in range(len(matrix)):
            min_ele.append(min(matrix[i]))
        max_ele = []
        for j in range(len(matrix[0])):
            re=0
            for i in range(len(matrix)):
                print(matrix[i][j])
                re = max(re,matrix[i][j])
            if re in min_ele:
                    return [re]
                    break        
