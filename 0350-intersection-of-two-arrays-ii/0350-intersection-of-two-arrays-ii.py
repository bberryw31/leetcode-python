class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count, nums2_count = {}, {}
        result = []
        for num1 in nums1:
            nums1_count[num1] = nums1_count.get(num1, 0) + 1
        for num2 in nums2:
            nums2_count[num2] = nums2_count.get(num2, 0) + 1
        for num in nums1_count:
            result.extend([num] * min(nums1_count.get(num, 0), nums2_count.get(num, 0)))
        return result