class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        count = 1

        def findBiggestJump(left, right):
            nonlocal count
            max_jump = (0, 0)
            if right >= len(nums) - 1:
                return count
            for i in range(left, right + 1):
                if i + nums[i] > max_jump[1]:
                    max_jump = (i + 1, i + nums[i])
            if max_jump[1] >= len(nums) - 1:
                return count + 1
            count += 1
            return findBiggestJump(max_jump[0], max_jump[1])
        
        return findBiggestJump(1, nums[0])