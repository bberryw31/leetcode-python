class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                # Check if number
                if board[row][col].isnumeric():
                    number = board[row][col] 
                else:
                    continue
                # Check boxes
                if number not in boxes[(col // 3) + 3 * (row // 3)]:
                    boxes[(col // 3) + 3 * (row // 3)].add(number)
                else:
                    return False
                # Check rows
                if number not in rows[row]:
                    rows[row].add(number)
                else:
                    return False
                # Check columns
                if number not in columns[col]:
                    columns[col].add(number)
                else:
                    return False
        return True

            