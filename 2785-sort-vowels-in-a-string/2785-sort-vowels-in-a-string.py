class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_indices = []
        vowels = []
        for i in range(len(s)):
            if s[i].lower() in {"a", "e", "i", "o", "u"}:
                vowel_indices.append(i)
                vowels.append(s[i])
        vowels.sort()
        result = []
        result.extend(s)
        for i in range(len(vowels)):
            result[vowel_indices[i]] = vowels[i]
        
        return "".join(result)
            
                