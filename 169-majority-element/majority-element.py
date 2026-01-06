class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        
        ans=-1
        temp = (len(nums))//2
        for i in dici:
            val=dici[i]
            if (val>temp):
                ans= i 
                break
        return ans