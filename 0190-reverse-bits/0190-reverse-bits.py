class Solution:
    def reverseBits(self, n: int) -> int:
        result = []
        binary = "{0:32b}".format(n)
        for num in binary[::-1]:
            if num == " ":
                result.append('0')
            else:
                result.append(num)
        result = ("".join(result))
        return int(result, 2)