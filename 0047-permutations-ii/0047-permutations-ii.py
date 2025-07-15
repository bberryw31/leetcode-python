class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def helper(numbers, temp):
            if len(temp) == len(nums):
                result.add(tuple(temp))
                return
            for i in range(len(numbers)):
                temp.append(numbers[i])
                helper(numbers[:i] + numbers[i + 1:], temp)
                temp.pop()
        helper(nums, [])
        return [list(element) for element in result]