class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1
        for i in range(1, n // 2 + 1):
            temp = factorial((n - 2 * i) + i)
            if i > 1:
                temp /= factorial(i)
            if n - 2 * i > 1:
                temp /= factorial(n - 2 * i)
            print(temp)
            res += temp
        return int(res)