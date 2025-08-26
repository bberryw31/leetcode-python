class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        base = image[sr][sc]
        def dfs(row, col):
            if row == m or row < 0 or col == n or col < 0 or image[row][col] != base:
                return
            image[row][col] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + dr, col + dc)
        if base == color:
            return image
        dfs(sr, sc)
        return image