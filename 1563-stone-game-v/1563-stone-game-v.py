class Solution:
    def stoneGameV(self, A):
        n = len(A)

        dp = [[0] * n for _ in range(n)]

        mx = [[0] * n for _ in range(n)]

        for i in range(n):
            mx[i][i] = A[i]

        for j in range(1, n):

            mid = j
            sm = A[j]
            right = 0

            for i in range(j - 1, -1, -1):

                sm += A[i]

                while mid > i and (right + A[mid]) * 2 <= sm:
                    right += A[mid]
                    mid -= 1

                # Equal case
                if right * 2 == sm:
                    dp[i][j] = mx[i][mid]

                # Left side is smaller
                if mid != i:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[i][mid - 1]
                    )

                # Right side is smaller
                if mid != j:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[j][mid + 1]
                    )

                # Maximum score + current interval sum
                mx[i][j] = max(
                    mx[i][j - 1],
                    dp[i][j] + sm
                )

                mx[j][i] = max(
                    mx[j][i + 1],
                    dp[i][j] + sm
                )

        return dp[0][n - 1]