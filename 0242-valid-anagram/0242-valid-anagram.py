class Solution(object):
    def isAnagram(self, s, t):

        if len(s)!=len(t):
            return False

        freq = {}
        # FREQ COUNT 
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # YAHA PAR FREQ DECREASE 
        for ch in t:
            if ch not in freq:
                return False
            if freq[ch] == 0:
                return False

            freq[ch] -= 1

        return True
            