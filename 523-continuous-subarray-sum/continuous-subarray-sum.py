class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq = { 0: -1 }
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            rem = curr % k
            if rem in freq:
                if i - freq[rem] > 1:
                    return True
            else:
                freq[rem] = i
        return False
        