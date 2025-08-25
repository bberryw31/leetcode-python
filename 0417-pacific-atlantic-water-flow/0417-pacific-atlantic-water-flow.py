class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights[0]), len(heights)
        # initialize graph with two bool per grid
        graph = [[[False, False] for _ in range(m)] for _ in range(n)]

        # initialize memoization of visited tiles with set
        visit = set()

        # initialize a queue to store tiles to visit
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        # iterate while item in queue
        while queue:
            # iterate over queue
            for i in range(len(queue)):
                # get last element in queue
                r, c = queue.popleft()

                # if tile adjacent to pacific ocean, set first bool to True
                if r == 0 or c == 0:
                    graph[r][c][0] = True
                
                # move to four directions
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # next if out of map or memoized
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or (nr, nc) in visit:
                        continue
                    
                    # if adjacent to pacific ocean or higher than previous, update graph
                    if heights[nr][nc] >= heights[r][c] or nr == 0 or nc == 0:
                        graph[nr][nc][0] = True

                        # append to queue to check its neighbors
                        queue.append((nr, nc))

                        # memoize
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
        
        # find all tiles with both bool as True
        result = []
        for r in range(n):
            for c in range(m):
                if graph[r][c][0] and graph[r][c][1]:
                    result.append([r, c])
        
        return result