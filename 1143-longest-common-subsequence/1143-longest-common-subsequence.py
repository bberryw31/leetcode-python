class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for row in range(1, len(text2) + 1):
            for col in range(1, len(text1) + 1):
                if text2[row - 1] == text1[col - 1]:
                    dp[row][col] = max(dp[row - 1][col - 1] + 1, dp[row - 1][col])
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
        return dp[-1][-1]
