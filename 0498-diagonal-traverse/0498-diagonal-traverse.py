class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        stack = [(0, 0)]
        visit = set()
        res = []
        direction = 1
        while stack:
            for r, c in stack[::direction]:
                res.append(mat[r][c])
            temp = []
            for r, c in stack:
                if r + 1 < row and (r + 1, c) not in visit:
                    temp.append((r + 1, c))
                    visit.add((r + 1, c))
                if c + 1 < col and (r, c + 1) not in visit:
                    temp.append((r, c + 1))
                    visit.add((r, c + 1))
            stack = temp[:]
            direction *= -1
        return res


                