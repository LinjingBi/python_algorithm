'''
用两个队列来实现一栈，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


class Solution:
    def __init__(self):
        self._q1 = []
        self._q2 = []

    def push(self, val):
        if self._q2:
            self._q1.append(self._q2.pop(0))
        self._q2.append(val)

    def pop(self):
        assert self._q2, 'the stack is empty'
        val = self._q2.pop(0)
        try:
            self._q2.append(self._q1.pop())
        except IndexError:
            pass
        return val

P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())