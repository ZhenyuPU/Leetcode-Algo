class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        有不同的结束方式。
        本题是每条边长度不断缩小，每次转折都对应着上下左右其中一个的变化，最终应该是上下左右归于一个值，只要某一个值发生了变化就停止
        分每条边记录矩阵
        """
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        ans = []
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            if up > down:   # 判断终止条件
                break
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:      # 判断终止条件
                break
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if down < up:          # 判断终止条件
                break
            for i in range(down, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:      # 判断终止条件
                break
        return ans