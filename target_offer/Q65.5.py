"""
滑动窗口找中值
"""
# 利用heapq库实现最小堆，最大堆
# 由于heapq.nlargest/nsmallest在需要排列的长度为迭代对象的长度时，和sorted一样
# 直接用的sorted, 类似于做一个总长为窗口长的大顶堆和小顶堆，实时产出每个窗口内的中值
import collections


class Solution2:
    def __init__(self):
        self.max = collections.deque()
        self.min = collections.deque()

    # 用sorted做，因为heapq.nlargest/nsmallest在k等于可迭代对象的长度时，就是sorted
    # 这也说明nlargest并不是简单的建堆，而是用堆给无序数组做了堆排序， 
    def find_window_mid(self, array, k):
        res = []
        if array and k and len(array) >= k:

            for i in range(len(array)):
                # 如果第一个k周期已经凑齐就快要开始删边界元素了
                if i - k >= 0:
                    if array[i-k] <= res[-1]:
                        self._delete(array[i-k])
                    else:
                        self._delete(array[i-k], flag=False)
                # 往里面添加元素
                self._build_heap(array[i])

                # 凑齐k个就开始添加中位值
                if i + 1 >= k:
                    res.append(self.max[0])
        return res

    def _delete(self, val, flag=True):
        hp = self.max if flag else self.min

        idx = hp.index(val)
        if len(hp) - 1 == idx:
            hp.pop()
        else:
            hp[-1], hp[idx] = hp[idx], hp[-1]
            hp.pop()
            a = sorted(hp, reverse=flag)
            if flag:
                self.max = collections.deque(a)
            else:
                self.min = collections.deque(a)

        self._balance()

    def _balance(self):
        if len(self.max) < len(self.min):
            num = self.min.popleft()
            self.max.append(num)
            self.max = collections.deque(sorted(self.max, reverse=True))
            # self.min = collections.deque(sorted(self.min))
        # 不要忘记是 >=
        elif len(self.max) >= len(self.min) + 2:
            num = self.max.popleft()
            self.min.append(num)
            # self.max = collections.deque(sorted(self.max, reverse=True))
            self.min = collections.deque(sorted(self.min))

    def _build_heap(self, num):
        if (len(self.max) + len(self.min)) % 2 == 0:
            if self.min and self.min[0] < num:
                self.min.append(num)
                # sorted(self.min)
                num = self.min.popleft()
                self.min = collections.deque(sorted(self.min))
            self.max.append(num)
            self.max = collections.deque(sorted(self.max, reverse=True))
        else:
            if num < self.max[0]:
                self.max.append(num)
                num = self.max.popleft()
                self.max = collections.deque(sorted(self.max, reverse=True))
            self.min.append(num)
            self.min = collections.deque(sorted(self.min))


# 自己创建一个heap类，实现堆中任意元素的删除

class _Heap:
    def __init__(self, flag=True):
        self._hp = []
        self.flag = 1 if flag else -1  # 默认是大顶堆

    def __len__(self):
        return len(self._hp)

    def add(self, val):
        self._hp.append(val)

        index = len(self) - 1
        self._upheap(index)

    def _upheap(self, index):
        while (index - 1) // 2 >= 0:
            parent = (index - 1) // 2
            if self.flag * self._hp[index] > self.flag * self._hp[parent]:
                self._hp[index], self._hp[parent] = self._hp[parent], self._hp[index]
                index = parent
            else:
                break

    def remove(self, val):
        # print(self._hp)

        index = self._hp.index(val)
        # 如果是最后一个就直接pop
        if index == len(self) - 1:
            self._hp.pop()
        else:
            self._hp[index], self._hp[-1] = self._hp[-1], self._hp[index]
            self._hp.pop()
            if index > 0 and self.flag * \
                    self._hp[index] > self.flag * self._hp[(index - 1) // 2]:
                self._upheap(index)
            else:
                self._downheap(index)

    def pop(self):
        assert len(self._hp) != 0, 'the heap is empty'

        result = self._hp[0]
        self._hp[0], self._hp[-1] = self._hp[-1], self._hp[0]
        self._hp.pop()
        self._downheap(0)
        return result

    def _downheap(self, index):
        while 2 * index + 1 < len(self):
            bigger = 2 * index + 1
            right = 2 * index + 2
            if right < len(self):
                if self.flag * self._hp[right] > self.flag * self._hp[bigger]:
                    bigger = right
            if self.flag * self._hp[bigger] > self.flag * self._hp[index]:
                self._hp[bigger], self._hp[index] = self._hp[index], self._hp[bigger]
                index = bigger
            else:
                break

    @property
    def top(self):
        assert len(self) != 0, 'the heap is empty'

        return self._hp[0]

    def __iter__(self):
        for each in self._hp:
            yield each


class Solution:
    def __init__(self):
        self.min = _Heap(flag=False)
        self.max = _Heap()

    def _build_hp(self, num):
        if (len(self.min) + len(self.max)) % 2 == 0:
            if self.min and self.min.top < num:
                self.min.add(num)
                num = self.min.pop()
            self.max.add(num)
        else:
            if num < self.max.top:
                self.max.add(num)
                num = self.max.pop()
            self.min.add(num)

    def _get_mid(self):
            return self.max.top

    def find_window_mid(self, array, size):
        res = []
        if array and size and len(array) >= size:
            for i in range(size):
                self._build_hp(array[i])
            res.append(self._get_mid())

            for i in range(size, len(array)):
                mid = res[-1]
                # 注意当size为奇数时，max包含了mid，所以当array[i-size]正好是mid时，
                # 应该在max中找mid，然后删除，所以应该是 <= 包含 =
                if array[i - size] <= mid:
                    self.max.remove(array[i - size])
                    if len(self.max) < len(self.min):
                        self.max.add(self.min.pop())

                else:
                    self.min.remove(array[i - size])

                    if len(self.min) == len(self.max) - 2:
                        self.min.add(self.max.pop())
                self._build_hp(array[i])
                res.append(self._get_mid())
        return res if res else None




s = Solution2()
print(s.find_window_mid([2, 3, 4, 2, 6, 2, 5, 1], 3))
