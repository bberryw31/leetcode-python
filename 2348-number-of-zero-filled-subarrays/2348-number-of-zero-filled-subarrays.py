class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        temp = 0
        for num in nums:
            if num == 0:
                temp += 1
            else:
                for i in range(1, temp + 1):
                    res += i
                temp = 0
        if temp:
            for i in range(1, temp + 1):
                    res += i
        return res
