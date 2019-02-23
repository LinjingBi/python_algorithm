'''
LRU 近期最少使用
'''
# 使用OrderedDict, 一个按照放入先后排序的dict, 位于OrderedDict末尾的元素表示最有可能被再次访问
import collections


class LRUCache:
    # size缓存大小
    def __init__(self, size):
        self._size = size
        self._cache = collections.OrderedDict()

    def __setitem__(self, key, value):
        if key in self._cache:
            self._cache.pop(key)
        elif self._size == len(self._cache):  # 如果内存已满，就要删除最久的键值对
            self._cache.popitem(last=False)   # last=True,表示弹出末尾的键值对类似栈的LIFO，last=False，弹出开头的键值对类似队列FIFO，符合LRU，最前面的表示最久没使用
        self._cache[key] = value  # set的数据就是现在访问的，也是最有可能被再次的访问的元素，通过set放在末尾

    def __getitem__(self, key):
        val = self._cache.pop(key)  # 如果key不存在会报keyerror
        self._cache[key] = val  # 因为被get访问过，key被重新放置到了末尾
        return val


# 不用OrderedDict
class LRUCache:

    class _Node:
        def __init__(self, prev=None, nex=None, value=None):
            self.prev = prev
            self.nex = nex
            self.value = value

        def __repr__(self):
            return '({}, {}, {})'.format(self.prev.value, self.nex.value, self.value)

    def __init__(self, size):
        assert isinstance(size, int) and size > 0, 'size must be a positive integer'
        self.size = size
        self._map = {}     # sequence: {key:_Node(pre, nex, key)}
        self._cache = {}   # real cache dict
        self._head = self._Node()
        self._tail = self._Node()
        self._head.nex = self._tail
        self._tail.prev = self._head

    def __setitem__(self, key, value):
        if key in self._map:
            self._delete(key)
        if len(self._map) == self.size:
            last = self._tail.prev
            self._delete(last.value)
        self._cache[key] = value
        self._map[key] = self._Node(self._head, self._head.nex, key)
        self._head.nex.prev = self._map[key]
        self._head.nex = self._map[key]

    def _delete(self, key):
        self._map[key].prev.nex, self._map[key].nex.prev = self._map[key].nex, self._map[key].prev
        del self._map[key]
        del self._cache[key]

    def __getitem__(self, key):
        val = self._cache[key]
        self._delete(key)
        self[key] = val
        return val

    def __repr__(self):
        return repr(self._cache)


lru = LRUCache(5)
for i in range(8):
    lru[i] = i+1
print(lru._map)
print(lru[3])
print(lru._map)