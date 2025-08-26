class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        result = 0
        for dimension in dimensions:
            curr_diag = sqrt(dimension[0] ** 2 + dimension[1] ** 2)
            if curr_diag > max_diag:
                max_diag = curr_diag
                result = dimension[0] * dimension[1]
            elif curr_diag == max_diag:
                curr_area = dimension[0] * dimension[1]
                if curr_area > result:
                    result = curr_area
        return result