class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        w_start, w_end, h_start, h_end = m, 0, n, 0
        for row in range(n):
            if not any(grid[row]):
                continue
            for col in range(m):
                if grid[row][col] == 1:
                    w_start = min(w_start, col)
                    h_start = min(h_start, row)
                    w_end = max(w_end, col)
                    h_end = max(h_end, row)
        return (w_end - w_start + 1) * (h_end - h_start + 1)


