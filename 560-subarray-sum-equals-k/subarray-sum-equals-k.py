class Solution(object):
    def subarraySum(self, nums, k):
        prefix=0
        count=0
        freq={0:1}
        for i in nums:
            prefix+=i
            need=prefix-k
            if need in freq:
                count+=freq[need]
            freq[prefix]=freq.get(prefix,0)+1

        return count

        