class Solution(object):

    def lexGreaterPermutation(self, s, target):
        
        n = len(s)

        # Frequency of characters in s
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Try to make the first difference as far right as possible
        for i in range(n - 1, -1, -1):

            # Fresh frequency for this attempt
            count = freq[:]

            # Match target[0 ... i-1]
            possible = True

            for j in range(i):
                idx = ord(target[j]) - ord('a')

                if count[idx] == 0:
                    possible = False
                    break

                count[idx] -= 1

            if not possible:
                continue

            # At position i, choose the smallest character
            # that is greater than target[i]
            target_idx = ord(target[i]) - ord('a')

            for c in range(target_idx + 1, 26):

                if count[c] > 0:

                    count[c] -= 1

                    # Build answer
                    ans = target[:i] + chr(c + ord('a'))

                    # Put remaining characters in sorted order
                    for k in range(26):
                        ans += chr(k + ord('a')) * count[k]

                    return ans

        return ""