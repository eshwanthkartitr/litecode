class Solution:
    def areaOfMaxDiagonal(self, dimension: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        for l, b in dimension:
            diag = (l ** 2 + b ** 2) ** 0.5
            area = l * b
            if diag > max_diag + 1e-7:
                max_diag = diag
                max_area = area
            elif abs(diag - max_diag) < 1e-7:
                max_area = max(max_area, area)
        return max_area
