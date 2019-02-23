'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''

'''
滑动窗户的个数为 len(array)-size+1
'''
import collections

class Solution:
    def maxInWindows(self, size, array):
        res = []
        if array and size and len(array) >= size:
            index = collections.deque()
            for i in range(len(array)):
                # 要把新元素放到它是那个位置最大的地方，index的最大长度就是size，也就是新元素是目前最小值，没人被删除
                while index and array[i] >= array[index[-1]]:
                    index.pop()
                # 这时要看开头的元素，是不是范围内，由于每次只移一位，如果有超限的，只有可能出现在头部，只有index头部有可能出现最老的元素
                # 因为根据上一个while，只要之前出现的比当下元素小的元素都被pop出去了，所以超限元素能被保留下来
                # 只能是因为它是最大的
                if index and i - index[0]+1 > size:
                    index.popleft()
                index.append(i)
                if i + 1 >= size:
                    mx = index[0]
                    res.append(array[mx])

        return res if res else None


s = Solution()
print(s.maxInWindows(3, [9,8,7,6,5,4,3,2,1]))