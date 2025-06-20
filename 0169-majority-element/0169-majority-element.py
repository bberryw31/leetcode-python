class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            if num_count[num] > len(nums) / 2:
                return num