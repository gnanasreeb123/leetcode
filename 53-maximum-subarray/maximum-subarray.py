class Solution(object):
    def maxSubArray(self, nums):
        currentsum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            currentsum=max(nums[i],currentsum+nums[i])
            if currentsum>maxsum:
                maxsum=currentsum
        return maxsum


        