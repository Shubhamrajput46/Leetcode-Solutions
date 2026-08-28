class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        from collections import Counter

        n = len(s)
        freq = Counter(s)

        odd = [c for c in freq if freq[c] % 2]

        # Palindrome possible hai ya nahi
        if n % 2 == 0:
            if len(odd) != 0:
                return ""
            middle = ""
        else:
            if len(odd) != 1:
                return ""
            middle = odd[0]

        # First half ki frequency
        half = [0] * 26

        for c in freq:
            half[ord(c) - ord('a')] = freq[c] // 2

        m = n // 2
        t = target[:m]

        # Check whether target ka first half possible hai
        remaining = half[:]
        possible = True

        for c in t:
            idx = ord(c) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        # Agar exact half possible hai aur palindrome > target hai
        if possible:
            p = t + middle + t[::-1]

            if p > target:
                return p

        # Rightmost position se greater character dhundo
        remaining = half[:]

        for c in t:
            remaining[ord(c) - ord('a')] -= 1

        for i in range(m - 1, -1, -1):

            idx = ord(t[i]) - ord('a')
            remaining[idx] += 1

            # Prefix valid hona chahiye
            if min(remaining) < 0:
                continue

            # Sabse chhota character jo t[i] se bada ho
            for c in range(idx + 1, 26):

                if remaining[c] > 0:

                    new_half = t[:i] + chr(c + ord('a'))

                    remaining[c] -= 1

                    # Baaki characters smallest order me
                    for x in range(26):
                        new_half += chr(x + ord('a')) * remaining[x]

                    return new_half + middle + new_half[::-1]

        return ""