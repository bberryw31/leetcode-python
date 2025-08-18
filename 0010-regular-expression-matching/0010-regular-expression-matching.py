class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == '.':
                for j in range(len(s)):
                    if dp[i][j]:
                        dp[i + 1][j + 1] = True
            elif p[i] == '*':
                for j in range(len(s) + 1):
                    if dp[i - 1][j]:
                        dp[i + 1][j] = True
                if p[i - 1] == '.':
                    prev = len(s) + 1
                    for j in range(len(s) + 1):
                        if dp[i][j]:
                            prev = j
                            break
                    for j in range(prev, len(s) + 1):
                        dp[i + 1][j] = True
                else:
                    prev = len(s) + 1
                    for j in range(len(s) + 1):
                        if dp[i][j]:
                            prev = j
                        for k in range(prev, len(s) + 1):
                            if s[k - 1] == s[prev - 1]:
                                dp[i + 1][k] = True
                            else:
                                break

            else:
                for j in range(len(s)):
                    if p[i] == s[j] and dp[i][j]:
                        dp[i + 1][j + 1] = True
        for d in dp:
            print(d)
        return dp[-1][-1]
                    
            
