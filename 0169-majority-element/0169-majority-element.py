class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initiate a hashmap to store the counts of nums elements
        num_count = {}
        # Iterate through nums once
        for num in nums:
            # Count the number
            num_count[num] = num_count.get(num, 0) + 1
            # If number count is greater than half the size of nums, return the number
            if num_count[num] > len(nums) / 2:
                return num