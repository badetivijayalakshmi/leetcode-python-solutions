class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        low=nums[0]
        for j in range(1,n):
            if low < nums[j]:
                res = nums[j] - low
                ans = max(ans, res)
            low=min(low,nums[j])
        return ans
        