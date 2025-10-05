class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        base = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            result += (ord(columnTitle[i]) - 64) * (26 ** base)
            base += 1
            print(result, base)
        return result