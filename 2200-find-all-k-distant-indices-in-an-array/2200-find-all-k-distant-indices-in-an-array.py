class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == key:
                result.extend([x for x in range(i - k, i + k + 1) if 0 <= x < len(nums)])
        return list(set(result))