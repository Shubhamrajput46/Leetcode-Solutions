class Solution(object):
    def getRow(self, rowIndex):
        result = [[1]]

        for i in range(1, rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result[rowIndex]
        