class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longer, shorter = (str1, str2) if len(str1) > len(str2) else (str2, str1)
        for i in range(len(shorter), 0, -1):
            base = shorter[:i]
            if len(longer) % len(base) == 0 and len(shorter) % len(base) == 0:
                if (len(longer) // len(base)) * base == longer and (len(shorter) // len(base)) * base == shorter:
                    return shorter[:i]
        return ""
            
        