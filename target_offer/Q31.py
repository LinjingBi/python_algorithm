'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''


# 利用？？定理，因为是找连续的子数组，遍历到第n个元素的时候，
# 包含第n个元素的最长数组的值：当第n个大于0时是F(n-1)+a[n],反之是a[n]。
# 又因为是连续的子数组，不用动态规划记录前几个最大值，
# 为负就不连续，不可能还有变长的希望，所以就保留一个最大值就可以了
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return
        if len(array) == 1:
            return array[0]
        curr = array[0]
        # 负无穷，如果改为0，就无法比较全负序列
        result = -float('inf')
        for i in range(1, len(array)):
            if array[i] > 0:
                # 有可能curr此时为负，
                # 而array[i]为正，此时不能单纯的让curr += array[i]
                curr = max(curr + array[i], array[i])
            else:
                curr = array[i]
            result = max(result, curr)
        return result

# 稍逊色的动态规划，
# 用长度为len(array)的数组保存以array[i]结尾的最长连续子数组，
# 然后max求最大值
# 时间还是O(n),空间也是O(n），不是最优
# 是人人为我型dp
    def dp(self, array):
        if not array:
            return
        if len(array) == 1:
            return array[0]
        lis = [array[0]]
        curr = array[0]
        for i in range(1, len(array)):
            if array[i] > 0:
                # 他自己或者+curr
                curr = max(array[i], curr + array[i])
                lis.append(curr)
            else:
                # 他自己，并且改变curr
                curr = array[i]
                lis.append(array[i])
        return max(lis)


alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray(alist))
print(s.dp(alist))
