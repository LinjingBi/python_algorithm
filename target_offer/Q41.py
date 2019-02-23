'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''
"""
两个指针，一个指向第一个，一个指向最后一个，小了low前移一个，大了high后移
和相等的两组数，相隔远的两个数乘积小，所以我们从两头开始找
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # 排除输入为None，输入数组不足两个元素，以及最大的两个数相加依旧小于sum
        if array:
            low = 0
            high = len(array)-1
            while low < high:
                temp = array[low] + array[high]
                if temp < tsum:
                    low += 1
                elif temp > tsum:
                    high -= 1
                else:
                    return [array[low], array[high]]
        return []


test = [1,2,5,6,9,10,15]
s = Solution()
print(s.FindNumbersWithSum(test, 15))

