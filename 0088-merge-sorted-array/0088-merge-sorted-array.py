class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first, second, index = m - 1, n - 1, m + n - 1
        if not n:
            return
        while nums2:
            if first < 0 or nums1[first] < nums2[second]:
                nums1[index] = nums2.pop()
                second -= 1
            else:
                nums1[index], nums1[first] = nums1[first], nums1[index]
                first -= 1
            index -= 1