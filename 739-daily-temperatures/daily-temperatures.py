class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                index = st.pop()
                res[index] = i - index
            st.append(i)
        return res
        