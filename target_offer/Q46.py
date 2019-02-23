'''
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
"""
python中
3 and 3 -> 3
0 and 0 -> 0
任何数字和它自己and输出都是他自己
两个不同数字，除0以外，and 输出 and右边的数
0 放在左边， 0 and 任意变量，定义没定义的 都直接输出0 不会看and右边的东西
"""


class Solution:
    def sum_solution(self, n):
        # 当n-1等于0时， n-1 and self.sum_solution(n-1),会在n-1为0时直接得到0
        # 而不会将n-1(0)带入sum_solution，从而终止递归。
        return n + (n - 1 and self.sum_solution(n - 1))


s = Solution()
print(s.sum_solution(5))
