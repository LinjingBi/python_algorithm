
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


class Solution:
    def minNumberInRotateArray(self, rotateArray):

        def inside(rotateArray):
            if len(rotateArray) == 0:
                return 0
            # if rotateArray[0] <= rotateArray[-1]:
            #     return rotateArray[0]
            elif len(rotateArray) <= 2:
                return min(rotateArray)
            mid = len(rotateArray) // 2
            if rotateArray[0] < rotateArray[mid]:
                return inside(rotateArray[mid+1:])
            elif rotateArray[0] > rotateArray[mid]:
                return inside(rotateArray[:mid+1])
            else:
                return min(inside(rotateArray[mid+1:]), inside(rotateArray[:mid+1]))
        return inside(rotateArray)



Test = Solution()
print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
print(Test.minNumberInRotateArray([]))
print(Test.minNumberInRotateArray([1]))