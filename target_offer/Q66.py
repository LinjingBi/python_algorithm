''''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 [[a b c e], [s f c s], [a d e e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

class Solution:
    def __init__(self):
        self.array = None
        self.col = None
        self.row = None
        self.path = None

    def find_path(self, array, path):
        if array and path:
            self.array = array
            self.col = len(array[0])
            self.row = len(array)
            self.path = path
            discov = [None] * self.col * self.row

            for i in range(self.row):
                for j in range(self.col):
                    if self._core(discov, i, j, 0):
                        return True
        return False

    def _core(self, discov, row, col, count):
        if count == len(self.path):
            return True
        if 0 <= row < self.row and 0 <= col < self.col and discov[self.col*row+col] is None and self.array[row][col] == self.path[count]:
            discov[self.col*row+col] = 1
            count += 1
            res = self._core(discov, row+1, col, count) \
                  or self._core(discov, row-1, col, count) \
                  or self._core(discov, row, col+1, count) \
                  or self._core(discov, row, col-1, count)
            if not res:
                discov[self.col * row + col] = None  # 如果这这一步的子步数都是False，那么这一步也不能算入匹配，也就被释放，当作没访问过
            return res
        return False



s = Solution()
print(s.find_path([['a','b','c','e'], ['s','f', 'c', 's'], ['a', 'd', 'e', 'e']], "bcced"))


