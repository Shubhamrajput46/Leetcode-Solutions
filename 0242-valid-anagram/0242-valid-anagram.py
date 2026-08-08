class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        if s==t and len(s)==len(t):
            return True
        return False        