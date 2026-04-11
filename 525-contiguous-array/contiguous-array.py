class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq = { 0 : -1 }
        curr = res = 0
        for num in range(len(nums)):
            if nums[num] == 0:
                curr += -1
            else:
                curr += 1
            if curr in freq:
                length = num - freq[curr]
                res = max(res,length)
            else:
                freq[curr] = num
        return res


        