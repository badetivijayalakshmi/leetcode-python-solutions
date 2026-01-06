class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        is_dict={}
        ans=0
        for i in nums:
            if i in is_dict:
                is_dict[i] +=1
            else:
                is_dict[i]=1
        for i in is_dict:
            n = is_dict[i]
            temp=n*(n-1)/2 
            ans=ans+temp       
        return (int(ans))