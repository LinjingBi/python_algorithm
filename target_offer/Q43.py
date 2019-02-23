'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
'''

class Solution:
    def multiply(self, A):
        if A == None or len(A) <= 0:
            return
        length = len(A)
        aList = [1] * length
        for i in range(1, length):
            aList[i] = aList[i-1] * A[i-1]
        temp = 1
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            aList[i] *= temp
        return aList

test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))