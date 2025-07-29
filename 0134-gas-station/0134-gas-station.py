class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        offsets = [gas_val - cost_val for gas_val, cost_val in zip(gas, cost)]
        offsets_deque = deque(offsets)
        tank, tank_val = [], 0
        start = 0
        while offsets_deque and start < len(gas) * 2:
            tank.append(offsets_deque.popleft())
            start += 1
            if tank_val + tank[-1] < 0:
                offsets_deque.extend(tank)
                tank, tank_val = [], 0
                continue
            tank_val += tank[-1]
        else:
            if len(tank) == len(gas):
                return start - len(gas)
            else:
                return -1
                