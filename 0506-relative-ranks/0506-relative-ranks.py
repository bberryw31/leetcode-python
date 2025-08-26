class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_heap = [(-score[i], i) for i in range(len(score))]
        heapify(score_heap)
        medals = ["Bronze Medal", "Silver Medal", "Gold Medal"]
        while score_heap:
            curr = heappop(score_heap)
            if medals:
                score[curr[1]] = medals.pop()
            else:
                score[curr[1]] = str(len(score) - len(score_heap))
        return score