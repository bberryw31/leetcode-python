class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        prev_row = [0] * (m - 1) + [1]
        for i in range(n - 1, -1, -1):
            curr_row = [0] * m
            curr_row[-1] = prev_row[-1] if not obstacleGrid[i][-1]
            for j in range(m - 2, -1, -1):
                curr_row[j] = 0 if obstacleGrid[i][j] else curr_row[j + 1] + prev_row[j]
            prev_row = curr_row[:]
        return curr_row[0]
