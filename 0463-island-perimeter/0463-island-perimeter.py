class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        perimeter = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if r + dr == row or r + dr < 0 or c + dc == col or c + dc < 0 or grid[r + dr][c + dc] == 0:
                            perimeter += 1
        return perimeter
                    