class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i, ch in enumerate(s):
            value = ord('z') - ord(ch) + 1
            position = i + 1

            ans += value * position

        return ans