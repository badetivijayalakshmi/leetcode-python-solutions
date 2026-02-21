class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        l = 0
        res = float("inf")
        for r in range(n):
            if (r-l == k):
                l += 1
            if (r-l+1 == k):
                res = min(res, nums[r] - nums[l])
        return res