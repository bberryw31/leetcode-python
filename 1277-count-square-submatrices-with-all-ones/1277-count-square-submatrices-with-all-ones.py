class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 0:
                    res += 1
                    if i and j:
                        left = matrix[i - 1][j]
                        up = matrix[i][j - 1]
                        dia = matrix[i - 1][j - 1]
                        if left > 0 and up > 0 and dia > 0:
                            offset = min(left, up, dia)
                            res += offset + 1 - matrix[i][j]
                            matrix[i][j] = offset + 1
        return res