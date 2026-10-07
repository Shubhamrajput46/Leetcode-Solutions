class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        for i in range(len(s) // 2):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

        