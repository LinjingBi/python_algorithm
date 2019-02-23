'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

# 快排O(n)和堆都可以。处理海量数据用堆排序（nlogk）。
# 相比于快排一次性把n都写入内存，在处理海量数据的时候并不明智。堆排序，可以设置一个大小为k的容器，将输入依次写入进行k个的堆排序，适合海量数据。


class Solution:
    def GetLeastNumbers(self, tinput, k):
        if not tinput or len(tinput) < k or k <= 0:
            return []
        import heapq
        hp = []
        for number in tinput[k:]:
            if len(hp) < k:
                hp.append(number)
            else:
                # 类比于原地建堆的思想，如果我们找最小堆，那么我们需要把最小值从堆顶也就是数组[0]放在数组末尾
                # 这样做出来的数列是从大到小排列，而这里要的输出是从小到大，我们必然需要.reverse()
                # 相比于建最大堆，最后成形就是从小到大，并不需要reverse。
                # 不过对heapq.nlargest/nsmallest来说,
                # 源码中都是利用了python的sorted(){sorted(iterable, key=key)[:n]/sorted(iterable, key=key, reverse=True)[:n]}，
                # smallest不用reverse，largest要。
                output = heapq.nsmallest(hp, k)
                if number < output[-1]:
                    output[-1] = number
        return output


tinput = [4, 5, 1, 6, 2, 7, 3, 8]
# s = Solution()
# print(s.GetLeastNumbers(tinput, 4))
# print(s.GetLeastNumbers(tinput, 5))


# 堆排序
def heapq_k(tinput, k):
    if not tinput or len(tinput) < k or k <= 0:
        return []
    hp = []
    for each in tinput:
        if len(hp) < k:
            hp.append(each)
        else:
            # 考虑把nsmallest放入下面的if，不做无效的堆排序，那么就需要添加一个等于k时，先做一个排序。
            output = nsmallest(hp)
            if output[-1] > each:
                output[-1] = each
    return output


def nsmallest(hp):
    for i in range((len(hp) - 2) // 2, -1, -1):
        heap_down(hp, len(hp), i)
    hp[0], hp[-1] = hp[-1], hp[0]
    for i in range(1, len(hp) - 1):
        # 如果要原地建堆，对于python中的数组来说，在函数间传递时，
        # 如果是整体传递，传递的是不经.copy()的指向同一个底层数组的副本，
        # 但如果用了切片（hp[:len(hp)-1])，那么就创建了一个新的底层数组了，
        # 不再是原地建堆，heap_down中所有对hp的操作，在本函数中都无效
        heap_down(hp, len(hp) - i, 0)
        hp[0], hp[len(hp) - 1 - i] = hp[len(hp) - 1 - i], hp[0]
    return hp


# 最大堆
def heap_down(hp, stop, i):
    while 2 * i + 1 < stop:
        large = 2 * i + 1
        if 2 * i + 2 < stop:
            if hp[large] < hp[2 * i + 2]:
                large = 2 * i + 2
        if hp[i] < hp[large]:
            hp[i], hp[large] = hp[large], hp[i]
            i = large
        else:
            break


print(heapq_k(tinput, 5))

# 快排做前k个最小, 没采用原地建堆


def quick_sort(tinput, k):
    import random
    if not tinput or not k or k > len(tinput) or k <= 0:
        return []
    pivot = random.choice(tinput)
    S = [each for each in tinput if each < pivot]
    E = [each for each in tinput if each == pivot]
    L = [each for each in tinput if each > pivot]

    if len(S) <= k:
        return quick_sort(S, k)
    elif len(S) < k <= len(S) + len(E):
        return pivot
    else:
        return quick_sort(L, k - len(S) - len(E))
