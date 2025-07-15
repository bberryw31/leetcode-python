class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        numbers = list(range(1, n +1))
        def helper(nums, temp):
            if len(temp) == k:
                result.append(temp[:])
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                helper(nums[i + 1:], temp)
                temp.pop()
        helper(numbers, [])
        return result