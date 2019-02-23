"""
找出递增序列中和为S的连续子序列(至少有两个数), 有几个就输出几个
"""
"""
跟上一道题类似，两个指针，第一个指向第一个，第二个指向第二个
如果小了，第二个指针前移，如果大了，第一个指针前移
"""
class Solution:
    def FindSubSequence(self, array, tsum):
        result = []
        if array and len(array) > 1:
            low = 0
            high = 1
            temp = sum(array[low:high+1])
            # 由于是递增序列，不存在相等的两个元素
            # 那么当array[low]==s/2时，就可以停止了
            # 因为此时high所指向的一定比s/2大，相加就更大于tsum
            # 为什么low必须小于high
            # 因为无论怎样low都是+1到等于high，所以说明high一定是大于tsum的，
            # 如果已经low-1到low==high，下一步如果要继续就是high+1，可是high已经大于tsum了，
            # high+1也于事无补，因为这是递增的数列，往后只会越来越大。
            while array[low] < (tsum+1)//2 and low < high < len(array):
                if temp < tsum:
                    high += 1
                    temp += array[high]
                else:
                    if temp == tsum:
                        result.append(array[low:high+1])
                    temp -= array[low]
                    low += 1
        return result

S=Solution()
print(S.FindSubSequence([1,2,3,4,5,6,7], 9))
print(S.FindSubSequence([4,4,4,4,4,4,4], 8)) #[[4,4]]




