class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [-count for count in task_count.values()]
        heapq.heapify(max_heap)
        queue = deque([])
        res = 0
        while max_heap or queue:
            for task in queue:
                task[1] -= 1
            if queue and queue[0][1] < 0:
                heapq.heappush(max_heap, -queue.popleft()[0])
            if not max_heap:
                res += 1
                continue
            priority_task = -heapq.heappop(max_heap)
            if priority_task - 1 > 0:
                queue.append([priority_task - 1, n])
            res += 1
        return res
