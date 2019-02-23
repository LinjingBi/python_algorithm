'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''


class Solution:
    def __init__(self):
        self._stack = []
        self._min = []  # 保存栈内每个元素所在时期的最大值

    def push(self, val):
        self._stack.append(val)
        # 比较后，存入val时期的最大
        if val <= self._min[-1]:
            self._min.append(val)
        else:
            self._min.append(self._min[-1])

    def pop(self):
        self._min.pop()
        return self._stack.pop()

    def top(self):
        return self._stack[-1]

    def min(self):
        return self._min[-1]
