class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        for i in range(len(nums)):
            if nums[i] == key:
                result.update(range(max(0, i - k), min(len(nums), i + k + 1)))
        return list(result)