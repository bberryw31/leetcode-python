class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(math.ceil(len(matrix) / 2)):
            for j in range(i, len(matrix) - i - 1):
                (
                    matrix[j][len(matrix) - 1 - i],
                    matrix[len(matrix) - 1 - i][len(matrix) - 1 - j],
                    matrix[len(matrix) - 1 - j][i],
                    matrix[i][j],
                ) = (
                    matrix[i][j],
                    matrix[j][len(matrix) - 1 - i],
                    matrix[len(matrix) - 1 - i][len(matrix) - 1 - j],
                    matrix[len(matrix) - 1 - j][i],
                )
