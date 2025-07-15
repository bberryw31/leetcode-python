class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = consonant = False
        index = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while index < len(word) and word[index].isalnum():
            if word[index].lower() in vowels:
                vowel = True
            elif word[index].isalpha():
                consonant = True
            index += 1
        else:
            if index < len(word):
                return False
        return vowel and consonant
