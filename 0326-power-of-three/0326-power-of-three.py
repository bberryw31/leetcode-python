class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        return n == 3 ** math.ceil(log(n, 3)) if n > 0 else False