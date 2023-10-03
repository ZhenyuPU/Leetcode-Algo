class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        找到下一步的规律：到底是往哪个方向
        方向：右，右上，下，左下
        边界判断：最后一行和最后一列
        """
        rows = len(mat)
        cols = len(mat[0])
        count = rows * cols
        x, y = 0, 0
        ans = []

        for i in range(count):
            ans.append(mat[x][y])

            if (x + y) % 2 == 0:
                # 最后一列
                if y == cols - 1:
                    x += 1
                # 第一行
                elif x == 0:
                    y += 1
                # 右上方向
                else:
                    x -= 1
                    y += 1
            else:
                # 最后一行
                if x == rows - 1:
                    y += 1
                # 第一列
                elif y == 0:
                    x += 1
                # 左下方向
                else:
                    x += 1
                    y -= 1
        return ans


if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    S = Solution()
    print(S.findDiagonalOrder(mat))
