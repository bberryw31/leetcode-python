class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        max_val = 0
        for i in range(len(nums)):
            dp[i + 1] = max(dp[i] + nums[i], nums[i])
            max_val = max(max_val, dp[i + 1])
        return max_val