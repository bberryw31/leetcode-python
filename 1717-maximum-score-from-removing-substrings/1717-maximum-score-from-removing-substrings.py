class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pre, post, pre_point, post_point = ('ab', 'ba', x, y) if x >= y else ('ba', 'ab', y, x)
        res = 0

        def helper(pool, target, point):
            nonlocal post, post_point, res
            stack = []
            for cha in pool:
                if cha == 'a' or cha == 'b':
                    if stack and cha == target[1] and stack[-1] == target[0]:
                        stack.pop()
                        res += point
                    else:
                        stack.append(cha)
                else:
                    helper(stack, post, post_point)
                    stack = []
            return stack
        helper(helper(s, pre, pre_point), post, post_point)
        return res
            
                

