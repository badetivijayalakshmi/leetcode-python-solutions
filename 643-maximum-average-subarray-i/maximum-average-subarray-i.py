class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k > n:
            return None
        else:
            current_sum = sum(nums[:k])
            max_sum = current_sum
            for i in range(k,n):
                current_sum += nums[i]
                current_sum -= nums[i-k] 
                max_sum = max(max_sum,current_sum)
            return max_sum / k