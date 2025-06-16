class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {s[0] : 1}
        max_length = 0
        left, right = 0, 1
        while right < len(s):
            most_frequent = max(char_count.values())
            if right - left - most_frequent <= k:
                max_length = max(max_length, right - left)
                right += 1
                char_count[s[right - 1]] = char_count.get(s[right - 1], 0) + 1
            else:
                char_count[s[left]] -= 1
                left += 1
        if right - left - most_frequent <= k:
            max_length = max(max_length, right - left)
        return max_length
