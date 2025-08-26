# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high, low = n, 1
        while high >= low:
            print(high, low)
            mid = (high + low) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                high = mid - 1
            else:
                low = mid + 1
        return high
