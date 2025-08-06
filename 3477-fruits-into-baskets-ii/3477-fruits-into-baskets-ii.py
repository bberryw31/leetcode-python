class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = len(fruits)
        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    count -= 1
                    baskets[i] = 0
                    break
        return count
                    
        
                
                    