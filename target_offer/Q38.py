'''
统计一个数字在排序数组中出现的次数。
'''


class Solution:
    def GetNumberOfK(self, data, k):
        number = 0
        if data:
            number = self.count_k(data, k, 0, len(data) - 1, 0)
        return number

    def count_k(self, data, k, start, end, count):
        # 此时的start>end一定是来自于start==上一一轮的mid or end == 上一轮的mid
        # 也就是上一轮的比较，以mid隔开的两区间有一个已经是mid==start或者mid==end状态了，
        # 那么这两个状态继续递归就会造成start>end的局面，而此时所有的比较已经在上一轮结束，
        # 所以直接返回count就可以了
        # 对于start==end，我们不做处理，因为mid==start==end，无论mid跟k关系如何，
        # 都会在下一轮变成start>end的局面，也就是下一轮在这里返回count
        if start > end:
            return count
        mid = (end + start) // 2
        if data[mid] == k:
            count += 1
            # 这里start和end的选取都要跳过mid
            count = self.count_k(data, k, start, mid - 1, count)
            count = self.count_k(data, k, mid + 1, end, count)
        elif data[mid] < k:
            count = self.count_k(data, k, mid + 1, end, count)
        else:
            count = self.count_k(data, k, start, mid - 1, count)

        return count


alist = [3, 3, 3, 3, 4, 6, 7, 8]
s = Solution()
print(s.GetNumberOfK(alist, 3))
import sys
sys.stdout.flush()
print()