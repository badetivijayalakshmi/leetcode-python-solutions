class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                x = stack.pop()
                result[x] = i-x
            stack.append(i)

        return result   