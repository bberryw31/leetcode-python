class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights[0]), len(heights)
        graph = [[[False, False] for _ in range(m)] for _ in range(n)]

        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == 0 or c == 0:
                    graph[r][c][0] = True

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or (nr, nc) in visit:
                        continue
                    if heights[nr][nc] >= heights[r][c] or nr == 0 or nc == 0:
                        graph[nr][nc][0] = True
                        queue.append((nr, nc))
                        visit.add((nr, nc))
        
        visit = set()
        queue = deque()
        queue.append((n - 1, m - 1))
        visit.add((n - 1, m - 1))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 or c == m - 1:
                    graph[r][c][1] = True

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or (nr, nc) in visit:
                        continue
                    if heights[nr][nc] >= heights[r][c] or nr == n - 1 or nc == m - 1:
                        graph[nr][nc][1] = True
                        queue.append((nr, nc))
                        visit.add((nr, nc))
        
        result = []
        for r in range(n):
            for c in range(m):
                if graph[r][c][0] and graph[r][c][1]:
                    result.append([r, c])
        
        return result