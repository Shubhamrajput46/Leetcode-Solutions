class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum palindromes using first i characters
        dp = [0] * (n + 1)

        for i in range(n):
            # Don't use s[i] as the end of a palindrome
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Try every palindrome starting at i
            for j in range(i + k - 1, n):
                if pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]