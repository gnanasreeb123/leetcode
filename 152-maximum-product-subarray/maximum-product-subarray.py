class Solution(object):
    def maxProduct(self, nums):
        ans=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            new_max=max(x,curr_min*x,curr_max*x)
            new_min=min(x,curr_min*x,curr_max*x)
            curr_max=new_max
            curr_min=new_min
            ans=max(curr_max,ans)
        return ans        