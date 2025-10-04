class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        new_mat = [[] for _ in range(r)]
        row_index = 0
        for row in range(len(mat)):
            for num in mat[row]:
                if len(new_mat[row_index]) == c:
                    row_index += 1
                new_mat[row_index].append(num)
        return new_mat