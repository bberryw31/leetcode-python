class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n <= 0 else int(math.log2(n)) == math.log2(n)