'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''

class Solution:
    def duplicate(self, array):
        if array:
            i = 0
            result = []
            while i < len(array):
                if array[i] != i:
                    if array[array[i]] != array[i]:
                        # 注意不能直接把array[i]带入，不然会造成混乱
                        index = array[i]
                        array[i], array[index] = array[index], array[i]
                        continue
                    elif array[i] not in result:
                        result.append(array[i])
                i += 1
            return result
        return None


test = [0,1,6,2,3,4,6,6]
s = Solution()
print(s.duplicate(test))



