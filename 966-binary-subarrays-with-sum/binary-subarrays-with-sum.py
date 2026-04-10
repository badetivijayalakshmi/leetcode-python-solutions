class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = { 0 : 1 }
        curr = count = 0
        for num in nums:
            curr += num
            if curr - goal in freq:
                count += freq[curr-goal]
            freq[curr] = freq.get(curr,0) + 1
        return count
        