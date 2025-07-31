class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_last_pos = {}
        for i in range(len(s)):
            char_last_pos[s[i]] = i
        start = 0
        count = 1
        max_substring = char_last_pos[s[0]]
        res = []
        while len(s) > start:
            if max_substring == start:
                res.append(count)
                count = 0
            start += 1
            count += 1
            if start == len(s):
                break
            max_substring = max(max_substring, char_last_pos[s[start]])
        return res
