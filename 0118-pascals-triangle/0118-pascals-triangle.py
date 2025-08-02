class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1, 1])
        if numRows == 2:
            return res
        prev = [1, 1]
        temp = []
        while len(temp) < numRows:
            temp = [1]
            for i in range(len(prev) - 1):
                temp.append(prev[i] + prev[i + 1])
            temp.append(1)
            res.append(temp)
            prev = temp[:]
        return res

        