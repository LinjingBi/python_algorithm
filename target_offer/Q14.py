'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

class Solution:
    # 一个类似于快排的方法, 只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变
    def reOrderArray(self, array):
        if len(array) < 2:
            return array
        low = 0
        high = len(array) - 1
        while low < high:
            if array[low] % 2 == 0:
                array[low], array[high] = array[high], array[low]
                high -= 1
            else:
                low += 1
        return array
test = Solution()
print(test.reOrderArray([2,3,1,3,8]))

