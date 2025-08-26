class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                slow, fast = i, i
                break
        else:
            return nums
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
        return nums
        