class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if gas == cost:
            return 0
        last_gas, last_cost = -1, -1
        for starting_point in range(len(gas)):
            if gas[starting_point] - cost[starting_point] <= 0:
                continue
            if gas[starting_point] == last_gas and cost[starting_point] == last_cost:
                continue
            last_gas, last_cost = gas[starting_point], cost[starting_point]
            tank = gas[starting_point]
            for index in range(len(gas)):
                next_cost = cost[(starting_point + index) % len(gas)]
                if tank >= next_cost:
                    tank -= next_cost
                    tank += gas[(starting_point + index + 1) % len(gas)]
                else:
                    break
            else:
                return starting_point
        else:
            return -1

