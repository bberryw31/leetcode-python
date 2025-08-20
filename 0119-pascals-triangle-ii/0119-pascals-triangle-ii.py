class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        res = [1, 1]
        for _ in range(rowIndex - 1):
            temp = [1]
            for i in range(len(res) - 1):
                temp.append(res[i] + res[i + 1])
            temp.append(1)
            res = temp[:]
        return res

