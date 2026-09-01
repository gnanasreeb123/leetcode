class Solution(object):
    def majorityElement(self, nums):
        freq={}
        ans=[]
        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        for i in freq:
            if freq[i]>len(nums)//3:
                ans.append(i)
        return ans
                
            
        