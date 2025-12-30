class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = math.inf
        for i in range(len(nums) - 2):
            sub_target = target - nums[i]
            low = i + 1
            high = len(nums) - 1
            while low < high:
                current_sum = nums[low] + nums[high]
                if current_sum < sub_target:
                    low += 1
                elif current_sum > sub_target:
                    high -= 1
                else:
                    return target
                if abs(min_diff) > abs(current_sum - sub_target):
                    min_diff = current_sum - sub_target
        return target + min_diff