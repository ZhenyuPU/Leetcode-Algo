class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        row = len(matrix)
        t = 0
        while row-2 > 0:
            for i in range(row-1):
                m_1 = matrix[t+i][t]
                m_2 = matrix[t+i][row-1+t]
                m_3 = matrix[row-1+t][row-1+t-i]
                m_4 = matrix[row-1+t-i][t]

                tmp = matrix[t][t+i]
                matrix[t][t+i] = matrix[row-1+t-i][t]
                matrix[row-1+t-i][t] = matrix[row-1+t][row-1+t-i]
                matrix[row-1+t][row-1+t-i] = matrix[t+i][row-1+t]
                matrix[t+i][row-1+t] = tmp
            row -= 2
            t += 1
            找到对应的旋转四个点，进行操作，
            并考虑不断缩小的边的循环不变式如何写
        """

        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


if __name__ == '__main__':
    matrix =[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    S = Solution()
    S.rotate(matrix)
    print(matrix)