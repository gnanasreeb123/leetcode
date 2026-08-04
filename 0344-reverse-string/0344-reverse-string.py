class Solution(object):
    def reverseString(self, s):
        t=[]
        for i in range(len(s)-1,-1,-1):
            t.append(s[i])
        for i in range(len(s)):
            s[i]=t[i]
        return s