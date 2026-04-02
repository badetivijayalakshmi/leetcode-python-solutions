class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        st = []
        res = [-1] * n
        for i in range(2*n):
            while st and nums[st[-1]] < nums[i % n]:
                index = st.pop()
                res[index] = nums[i % n]
            if i < n:
                st.append(i)
        return res
        