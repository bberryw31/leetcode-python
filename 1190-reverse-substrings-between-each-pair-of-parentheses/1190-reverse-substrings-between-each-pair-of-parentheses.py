class Solution:
    def reverseParentheses(self, s: str) -> str:
        def flip(i):
            idx = i
            sub = []
            while s[idx] != ')':
                print(idx, sub)
                if s[idx] ==  '(':
                    subsub, idx = flip(idx + 1)
                    sub.extend(subsub)
                else:
                    sub.append(s[idx])
                    idx += 1
            sub.reverse()
            return sub, idx + 1

        res = []
        idx = 0
        while idx < len(s):
            if s[idx] == '(':
                sub, idx = flip(idx + 1)
                res.extend(sub)
            else:
                res.append(s[idx])
                idx += 1
        return ''.join(res)
