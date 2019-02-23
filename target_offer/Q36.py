'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''

'''
其实就是给无序数组排序，由于相等不算，所以我们要选择稳定性好的算法，那么就是归并排序。
一旦出现了交换，就说明有逆序对，但是逆序对个数跟交换的次数不相等，例如
按照归并的思想，我现在有一个前半段和一个后半段的序列，要来归并合二为一
5678 1234
我们从第一位开始，5>1, 可是5却在低位，说明要交换一次，那么这次逆序带给我们多少个逆序对呢
5678 分别和 1 组成了四对逆序对，所以出现交换，我们逆序对的数目应该增加len(前半段）-i（前半段当前比较元素下标），而不是单纯的+1

'''
# 归并排序
# class Solution:
#     def InversePairs(self, array):
#         if not array:
#             return 0
#
#         if len(array) == 1:
#             return array
#
#         mid = len(array)//2
#
#         front = self.InversePairs(array[:mid])
#         back = self.InversePairs(array[mid:])
#
#         self._merge(front, back, array)
#
#         return array
#
#     def _merge(self, front, back, array):
#         i = 0
#         j = 0
#         while i + j < len(array):
#             if i == len(front) or (j < len(back) and back[j] < front[i]):
#                 array[i+j] = back[j]
#                 j += 1
#             else:
#                 array[i+j] = front[i]
#                 i += 1

#


class Solution:
    def InversePairs(self, array):
        if not array:
            return 0
        return self._merge_sort(array)

    def _merge_sort(self, array):
        if len(array) == 1:
            return 0

        mid = len(array) // 2
        front = array[:mid]
        back = array[mid:]

        left = self.InversePairs(front)
        right = self.InversePairs(back)

        count = self._merge(front, back, array, left+right)
        # 这里不需要return array因为，array指向的底层数组在merge里面已经被改写，
        # 也就是说入参array，经过前后两个子数组的归并在merge中已经被改变了
        # python中，数组在函数间传递，只要不是数组的切片形式，
        # 传递的都是指向底层数组的指针，也就是说所有函数共享一个底层数组，
        # 在一个函数里该数组被改变，所有函数里的该数组都变
        return count

    def _merge(self, front, back, array, count):
        i = 0
        j = 0
        while i + j < len(array):
            # 这里的逻辑顺序不能变，因为在python里if语句判断or，只要第一个条件满足，就不会看后面的
            # 所以当i=len(front）时，并不会因为or后面的front[i]而报错
            # 同样and两端的语句，当j=0的值比front全部都小时，在j已经等于len(back)时，i依然<len(front),
            # 那么if会看or后面的内容，这时如果我们把back[j]<front[i]放前面，就会因为back超限而报错
            # 如果我们把j < len(back)放在第一位，if一看and第一个不满足，就会跳过if执行else，而不是继续看完if的条件语句
            if i == len(front) or (j < len(back) and back[j] < front[i]):
                array[i + j] = back[j]
                # 注意当i==len(front),j接着写入array是顺序的，不存在逆序
                # 所以我们只考虑i<len(front)的时候
                if i < len(front):
                    # 只用考虑i此时剩余的个数，不要在后面+j，因为j中都是顺序的，逆序只存在于ij之间
                    count += len(front) - i
                j += 1

            else:
                array[i + j] = front[i]
                i += 1
        return count


s = Solution()
print(s.InversePairs([2,1,3,1]))
