from bisect import bisect_right


class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # [start, end, weight, original_index]
        arr = []

        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by start, then end, then weight, then index
        arr.sort()

        starts = [x[0] for x in arr]

        memo = {}

        def better(a, b):
            """
            a and b = (score, indices)

            Return the one with:
            1. Higher score
            2. If score same -> lexicographically smaller indices
            """
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        def dfs(i, k):

            # No more intervals OR already selected 4
            if i == n or k == 4:
                return (0, ())

            if (i, k) in memo:
                return memo[(i, k)]

            # --------------------------------
            # Option 1: Don't take this interval
            # --------------------------------
            skip = dfs(i + 1, k)

            # --------------------------------
            # Option 2: Take this interval
            # --------------------------------
            l, r, w, idx = arr[i]

            # Need next.start > current.end
            next_i = bisect_right(starts, r)

            next_score, next_indices = dfs(next_i, k + 1)

            take = (
                w + next_score,
                tuple(sorted((idx,) + next_indices))
            )

            # Choose best
            ans = better(take, skip)

            memo[(i, k)] = ans

            return ans

        score, indices = dfs(0, 0)

        return list(indices)