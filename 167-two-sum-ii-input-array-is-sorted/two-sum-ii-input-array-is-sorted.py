class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return ([l+1,r+1])
                break
            elif sum < target:
                l += 1
            else:
                r -= 1
                
        