class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):

        n = len(nums)

        # value + original index
        arr = [(nums[i], i) for i in range(n)]

        # Values ke according sort
        arr.sort()

        ans = [0] * n

        i = 0

        while i < n:

            j = i

            # Ek connected group find karo
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Group values
            values = []

            # Group original indices
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            # Original indices ko sort karo
            indices.sort()

            # Smallest values -> smallest indices
            for k in range(len(values)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans