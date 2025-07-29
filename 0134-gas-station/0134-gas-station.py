class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        start = 0
        while start < len(gas):
            if gas[start] < cost[start]:
                start += 1
                continue
            tank = gas[start]
            for i in range(len(cost)):
                tank -= cost[(start + i) % len(cost)]
                if tank < 0:
                    start += i
                    break
                tank += gas[(start + i + 1) % len(cost)]
            else:
                return start
        else:
            return -1
            