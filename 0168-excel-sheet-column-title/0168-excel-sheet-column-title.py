class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        if columnNumber == 1:
            return "A"
        while columnNumber:
            current = columnNumber % 26
            if not current:
                result.append("Z")
                columnNumber = columnNumber // 26 - 1
            else:
                result.append(chr(64 + current))
                columnNumber = columnNumber // 26
            print(result, columnNumber)
        return "".join(result[::-1])

