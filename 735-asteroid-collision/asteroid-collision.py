class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            alive = True
            while stack and x < 0 and stack[-1] > 0:
                if abs(x) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(x) == abs(stack[-1]):
                    stack.pop()
                alive = False
                break
            if alive:
                stack.append(x)
        return stack
        