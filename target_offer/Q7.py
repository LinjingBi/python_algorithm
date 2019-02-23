'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


class Solution:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def push(self, val):
        self._stack1.append(val)

    def pop(self):
        try:
            return self._stack2.pop()
        except IndexError:
            pass
        assert len(self._stack1) != 0, 'the queue is empty'
        while self._stack1:
            self._stack2.append(self._stack1.pop())
        return self._stack2.pop()


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
