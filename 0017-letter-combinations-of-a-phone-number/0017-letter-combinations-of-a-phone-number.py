class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        combination_count = 1
        for digit in digits:
            if digit == "9" or digit == "7":
                combination_count *= 4
            else :
                combination_count *= 3

        combinations = [[] for i in range(combination_count)]

        repetition_counter = combination_count
        for i in range(len(digits)):
            letters = num_to_letter[int(digits[i])]
            letters_count = len(letters)
            repetition_counter /= letters_count
            for j in range(combination_count):
                letter_index = int(((j + 1) // repetition_counter) % letters_count)
                combinations[j].append(letters[letter_index])
                
        result = []
        for combination in combinations:
            result.append("".join(combination))
        if combination_count == 1:
            return []
        return result
            