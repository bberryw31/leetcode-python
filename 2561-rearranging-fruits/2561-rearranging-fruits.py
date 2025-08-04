from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        all_fruits = set(basket1 + basket2)
        total_counts = Counter(basket1 + basket2)
        
        for fruit, total_count in total_counts.items():
            if total_count % 2 == 1:
                return -1
        
        target_counts = {fruit: count // 2 for fruit, count in total_counts.items()}

        surplus_basket1 = []
        for fruit in all_fruits:
            current_count = count1.get(fruit, 0)
            target_count = target_counts[fruit]
            excess = current_count - target_count
            if excess > 0:
                surplus_basket1.extend([fruit] * excess)
        
        deficit_basket1 = []
        for fruit in all_fruits:
            current_count = count1.get(fruit, 0)
            target_count = target_counts[fruit]
            
            deficit = target_count - current_count
            if deficit > 0:
                deficit_basket1.extend([fruit] * deficit)
        
        surplus_basket1.sort()
        deficit_basket1.sort(reverse=True)
        global_min_cost = min(total_counts.keys())
        total_cost = 0
        
        for surplus_fruit, deficit_fruit in zip(surplus_basket1, deficit_basket1):
            total_cost += min(min(surplus_fruit, deficit_fruit), 2 * global_min_cost)
        
        return total_cost