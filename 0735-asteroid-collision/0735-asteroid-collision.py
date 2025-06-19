class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if stack == []:
                stack.append(asteroid)
            else:
                if asteroid * stack[-1] > 0:
                    stack.append(asteroid)
                else:
                    if asteroid > 0:
                        stack.append(asteroid)
                    else:
                        while True:
                            if asteroid * stack[-1] < 0:
                                if abs(asteroid) > abs(stack[-1]):
                                    stack.pop()
                                    if not stack:
                                        stack.append(asteroid)
                                        break
                                elif abs(asteroid) == abs(stack[-1]):
                                    stack.pop()
                                    break
                                else:
                                    break
                            else:
                                stack.append(asteroid)
                                break
        return stack