class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        prev_asteroids = asteroids[:]
        while True:
            stack = []
            for asteroid in prev_asteroids:
                if stack == []:
                    stack.append(asteroid)
                else:
                    if asteroid * stack[-1] > 0:
                        stack.append(asteroid)
                    else:
                        if asteroid > stack[-1]:
                            stack.append(asteroid)
                            continue
                        if abs(asteroid) > abs(stack[-1]):
                            stack.pop()
                            stack.append(asteroid)
                        elif abs(asteroid) == abs(stack[-1]):
                            stack.pop()
            if stack == prev_asteroids:
                break
            prev_asteroids = stack[:]
        return stack