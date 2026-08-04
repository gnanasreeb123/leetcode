class Solution(object):
    def findMissingElements(self, nums):
        unique=[]
        m=max(nums)
        n=min(nums)
        for i in range(n,m+1):
            if i not in nums:
                unique.append(i)
        return unique