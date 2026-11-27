class Solution:
    def beautySum(self, s):
        total = 0

        for i in range(len(s)):
            freq = {}

            for j in range(i, len(s)):
                ch = s[j]

                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1

                maximum = max(freq.values())
                minimum = min(freq.values())

                total += maximum - minimum

        return total