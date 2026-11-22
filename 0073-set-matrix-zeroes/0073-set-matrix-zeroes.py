class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = []
        zero_cols = []

        # Step 1: Find all original zeroes
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)

        # Step 2: Make those rows zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Step 3: Make those columns zero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0