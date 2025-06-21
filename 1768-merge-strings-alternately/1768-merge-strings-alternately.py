class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_index, word2_index = 0, 0
        result = []
        while word1_index < len(word1) or word2_index < len(word2):
            if word1_index < len(word1):
                result.append(word1[word1_index])
                word1_index += 1
            if word2_index < len(word2):
                result.append(word2[word2_index])
                word2_index += 1
        return "".join(result)
        
