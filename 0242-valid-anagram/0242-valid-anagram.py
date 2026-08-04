class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for ch in s:
            if ch in d1:
                d1[ch]+=1
            else:
                d1[ch]=1
        for ch in t:
            if ch in d2:
                d2[ch]+=1
            else:
                d2[ch]=1
        return d1==d2