class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottles_drunk = empty_bottles = numBottles
        full_bottles = 0
        while full_bottles + empty_bottles:
            if empty_bottles >= numExchange:
                empty_bottles -= numExchange
                full_bottles += 1
                numExchange += 1
            elif full_bottles:
                bottles_drunk += full_bottles
                empty_bottles += full_bottles
                full_bottles = 0
            else:
                break
        return bottles_drunk
            