class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if target==nums[i]:
                return i
        else:
            return -1
        