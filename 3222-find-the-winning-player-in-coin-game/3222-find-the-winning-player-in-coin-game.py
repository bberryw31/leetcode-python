class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if x >= y // 4:
            return "Alice" if (y // 4) % 2 else "Bob"
        else:
            return "Alice" if x % 2 else "Bob"