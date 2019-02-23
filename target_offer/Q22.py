'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []
        # 不反向，每次就要pop(0)这样对数组来说很耗时。所以先reverse
        popV.reverse()
        # 不管什么样的popV都来自于push的过程
        # 所以利用stack和pushV重建整个push过程
        # 然后从push的第一个元素开始和popV的第一个（reverse后的最后一个）进行比较
        # 一致就双双弹出，并且继续比较(while)，因为很有可能有连续的pop存在于push的过程中
        for i in pushV:
            stack.append(i)
            while len(stack) > 0 and stack[-1] == popV[-1]:
                stack.pop()
                popV.pop()
        # 由于长度一致并且同时执行pop，一个为空表示都为空
        return False if stack else True


pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popV))





