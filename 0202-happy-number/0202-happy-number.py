class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while 1:
            square_sum = 0
            for num in str(n):
                square_sum += int(num) ** 2
            if square_sum == 1:
                return True
            if square_sum in visited:
                return False
            visited.add(square_sum)
            n = square_sum