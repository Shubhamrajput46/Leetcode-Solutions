class Solution(object):
    def reverseWords(self, s):
        s=s.strip()
        s=s.split()

        s.reverse()

        return " ".join(s)         
        