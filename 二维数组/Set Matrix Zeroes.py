class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先判断边界是否有0，不然当先找到内点为0，把值设为0的时候，就不好判断边界该不该设为0
        当内部点找到为0的时候，先不要急着把横竖设为0，先找到这些点，并用某种方式标记，然后再重新用循环设为0，不然找到一个点就设置为0，
        那么就不好找到下一个为0的点了。
        """
        m = len(matrix)
        n = len(matrix[0])
        flag_col0 = False
        flag_row0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                flag_row0 = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0

if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s = Solution()
    s.setZeroes(matrix)
    print(matrix)