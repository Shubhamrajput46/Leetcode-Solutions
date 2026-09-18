class Solution(object):
    def maxNumOfSubstrings(self, s):
        first = [-1] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')

            if first[idx] == -1:
                first[idx] = i

            last[idx] = i

        # Find valid intervals
        intervals = []

        for c in range(26):

            if first[c] == -1:
                continue

            start = first[c]
            end = last[c]

            i = start
            valid = True

            while i <= end:
                idx = ord(s[i]) - ord('a')

                # Character appeared before our start
                if first[idx] < start:
                    valid = False
                    break

                end = max(end, last[idx])
                i += 1

            if valid:
                intervals.append([start, end])

        # Choose maximum number of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result
        