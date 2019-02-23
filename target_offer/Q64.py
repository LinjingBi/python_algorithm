'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''

"""
分为两个堆 最大堆 最小堆
最大堆(max)保存前n/2，保证堆顶是前n/2的最大值
最小堆(min)保存后n/2，保证堆顶是后n/2的最小值
始转保证两个堆大小相差不超过1，当相差1时，max（前n/2）比min多一个
当n是奇数的时候，
理应将num放入min，让min，max相等。但如果此时的num小于max的top，说明它属于前n/2(max)，
那么此时先将num放入max，max向上冒泡完毕后，将max的top移入min，进行向上冒泡，从而两堆长度一致
如果num大于max的top，num直接被放入min
当n是偶数的时候，
理应将num放入max，但如果num大于min的top，就应该先放入min，然后将min的top移入max，
如果num小于min的top，就可以直接放入max。
"""

"""
注意python的assert用法
assert 条件语句，‘当条件语句不满足时报错的内容’
一定是不满足条件语句，才会报错，而不是满足才报错
"""


class Solution:

    class _Heap:
        def __init__(self, flag=True):
            # flag为True 为大顶堆，top是最大值
            self.flag = 1 if flag else -1
            self._heap = []

        def __len__(self):
            return len(self._heap)

        def add(self, val):
            self._heap.append(val)

            index = len(self) - 1

            while (index - 1) // 2 >= 0:
                parent = (index - 1) // 2
                if self.flag * \
                        self._heap[index] > self.flag * self._heap[parent]:
                    self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
                    index = parent
                else:
                    break

        @property
        def top(self):
            # 注意assert，后面的条件不满足，才会报错，而不是满足报错
            assert len(self) != 0, 'the heap is empty'
            return self._heap[0]

        def pop(self):
            assert len(self._heap) != 0, 'the heap is empty'

            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            result = self._heap.pop()

            index = 0
            while 2 * index + 1 < len(self):
                bigger = 2 * index + 1
                if 2 * index + 2 < len(self):
                    if self.flag * \
                            self._heap[bigger] < self.flag * self._heap[2 * index + 2]:
                        bigger = 2 * index + 2
                if self.flag * \
                        self._heap[index] < self.flag * self._heap[bigger]:
                    self._heap[index], self._heap[bigger] = self._heap[bigger], self._heap[index]
                    index = bigger
                else:
                    break
            return result

        def __repr__(self):
            return self._heap.__repr__()

        def __iter__(self):
            for each in self._heap:
                yield each

    def __init__(self):
        # max是一个大顶堆，存放前n/2小的数据，top为前n/2的最大值
        # min是一个小顶堆，用于存放后n/2大的数据，top为后n/2的最小值
        self.max = self._Heap()
        self.min = self._Heap(flag=False)

    # max应该是保存数据最多的
    def insert(self, num):
        # 长度为偶数或0的时候，num要进入max
        if (len(self.max) + len(self.min)) % 2 == 0:
            # 一般情况长度为偶数时，加入num应该放入max，也就是前n/2
            # 但是如果这个值大于min（后n/2)的top，它应该放入min
            # 我们就先把它放入min，然后把min的top当作新的num，加入max
            # 这样max依旧比min多一个数
            if len(self.min) > 0 and num > self.min.top:
                self.min.add(num)
                # 添加完毕后，移除top给max
                num = self.min.pop()
            self.max.add(num)
        else:
            # 如果总数是奇数，那么一定是大顶堆多1，此时就应该小顶堆+1
            # 但如果num比max的top小，num就应该加入大顶堆，而不是小顶堆
            # 此时我们先让num加入大顶堆，然后将大顶堆的top转让给小顶堆
            # 这样大家就一样长了
            # 这里不存在len(max)小于零，因为第一个num一定是给max，
            # 所以为奇数时，max不会为空，至少有一个元素
            if num < self.max.top:
                self.max.add(num)
                num = self.max.pop()
            self.min.add(num)

    def get_min(self):
        if (len(self.max) + len(self.min)) % 2 == 0:
            return (self.max.top + self.min.top) / 2
        else:
            return self.max.top


s = Solution()
e = [1, 3, 2, 4, 6, 7, 5, 8]
for i in e:
    s.insert(i)
print(s.get_min())
for i in s.max:
    print(i)
