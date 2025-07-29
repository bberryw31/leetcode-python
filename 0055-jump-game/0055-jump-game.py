class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = 0
        for i in range(1, len(nums)):
            if nums[-i -1] >= i - target:
                target = i
        return True if nums[0] >= len(nums) - target or len(nums) < 2 else False