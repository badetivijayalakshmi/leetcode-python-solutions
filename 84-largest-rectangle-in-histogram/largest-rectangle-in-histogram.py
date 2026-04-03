class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        n = len(heights)
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                h = heights[st.pop()]
                if not st:
                    w = i
                else:
                    w = i - st[-1] - 1
                max_area = max(max_area, h*w)

            st.append(i)
        while st:
            h = heights[st.pop()]
            if not st:
                w = n
            else:
                w = n - st[-1] - 1
            max_area = max(max_area,h*w)
        return max_area

