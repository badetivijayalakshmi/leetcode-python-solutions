class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = 0
        c1 = 0
        c2 = 0
        x = 0
        n = len(a)
        for i in range(n):
            if a[i] == 0:
                c0 += 1
            elif a[i] == 1:
                c1 += 1
            else:
                c2 += 1
        for _ in range(c0):
            a[x] = 0
            x += 1
        for _ in range(c1):
            a[x] = 1
            x += 1
        for _ in range(c2):
            a[x] = 2
            x += 1
