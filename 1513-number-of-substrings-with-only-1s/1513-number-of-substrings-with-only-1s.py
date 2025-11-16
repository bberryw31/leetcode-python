class Solution:    
    def numSub(self, s: str) -> int:
        bit_counter = 0
        ones = []
        for bit in s:
            if bit == '0':
                if bit_counter != 0:
                    ones.append(bit_counter)
                bit_counter = 0
            if bit == '1':
                bit_counter += 1
        if bit_counter != 0:
            ones.append(bit_counter)
        total_ones = 0
        for one in ones:
            total_ones += (one * (one + 1)) // 2
        return total_ones % (10 ** 9 + 7)