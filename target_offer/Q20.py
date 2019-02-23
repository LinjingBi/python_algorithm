
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''


class Solution:
    # 上下左右写四个循环
    def printMatrix(self, matrix):
        if not matrix:
            return []
        result = []
        x_min = 0
        x_max = len(matrix[0]) - 1
        y_min = 0
        y_max = len(matrix) - 1
        while len(result) != len(matrix) * len(matrix[0]):
            # 每行最后一个不扫
            for i in range(x_min, x_max):
                result.append(matrix[y_min][i])
            # 每列最后一个不扫
            for i in range(y_min, y_max):
                result.append(matrix[i][x_max])
            # 由于上面两个循环，导致我们再面对一维数组时，总会行/列差末尾的一个要放在下面扫
            # 只有一行时，行最后一个在这里扫[0][-1]，由于这种情况下只有最后一个所以要判断result的长度，及时停止
            for i in range(x_min, x_max):
                if len(result) != len(matrix) * len(matrix[0]):
                    result.append(matrix[y_max][-i - 1])
            # 只有一列时，列最后一个在这里扫[-1][0]
            for i in range(y_min, y_max):
                if len(result) != len(matrix) * len(matrix[0]):
                    print(matrix[-i - 1][x_min])
                    result.append(matrix[-i - 1][x_min])

            x_min += 1
            x_max -= 1
            y_min += 1
            y_max -= 1
        return result


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1], [2], [3], [4], [5]]
matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
S = Solution()
print(S.printMatrix(matrix))
print(S.printMatrix(matrix2))
print(S.printMatrix(matrix3))
