class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        m, n = len(grid[0]), len(grid)

        def isIsland(r, c):
            if r < 0 or c < 0 or r >= n or c >= m or (r, c) in visit or grid[r][c] == '0':
                return
            visit.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                isIsland(r + dr, c + dc)
            return 1
        
        result = 0
        for r in range(n):
            for c in range(m):
                res = isIsland(r, c)
                if res:
                    result += res
        
        return result


                