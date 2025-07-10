class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        max_left, max_right = height[left], height[right]
        while left < right:
            left += 1
            max_left = max(max_left, height[left])
            res += max_left - height[left]

            right -= 1 
            max_right = max(max_right, height[right])
            res += max_right - height[right]

        return res