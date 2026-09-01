class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        ans=0
        for x in s:
            if x-1 not in s:
                len=1
                cur=x

                while cur+1 in s:
                    len+=1
                    cur+=1
                ans=max(len,ans)
        return ans
                