class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #c0 = c1 = c2 = 0
        #x = 0
        #n = len(nums)
        #for i in range(n):
        #    if nums[i] == 0:
        #        c0 += 1
        #    elif nums[i] == 1:
        #        c1 += 1
        #    else:
        #        c2 += 1
        #for _ in range(c0):
        #    nums[x] = 0
        #    x += 1
        #for _ in range(c1):
        #    nums[x] = 1
        #    x += 1
        #for _ in range(c2):
        #    nums[x] = 2
        #    x += 1
#Dutch National Flag algo
        low = 0
        mid = 0
        high = len(a) - 1
        
        while mid <= high:
            if a[mid] == 0:
                a[low], a[mid] = a[mid], a[low]
                low += 1
                mid += 1
        
            elif a[mid] == 1:
                mid += 1
        
            else:  # a[mid] == 2
                a[mid], a[high] = a[high], a[mid]
                high -= 1
