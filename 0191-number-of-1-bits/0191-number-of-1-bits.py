class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = "{0:32b}".format(n)
        count = 0
        for bit in binary:
            if bit == '1':
                count += 1
        return count