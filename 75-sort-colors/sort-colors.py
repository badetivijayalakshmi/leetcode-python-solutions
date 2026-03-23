class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        x = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1
            else:
                c2 += 1
        for _ in range(c0):
            nums[x] = 0
            x += 1
        for _ in range(c1):
            nums[x] = 1
            x += 1
        for _ in range(c2):
            nums[x] = 2
            x += 1
