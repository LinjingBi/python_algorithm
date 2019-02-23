'''
quick sort
'''

#
# def quick_sort(array):
#     s = len(array)
#     if s < 2:
#         return array
#     less = []
#     equal = []
#     large = []
#     for each in array:
#         if each < array[0]:
#             less.append(each)
#         elif each == array[0]:
#             equal.append(each)
#         else:
#             large.append(each)
#     return quick_sort(less)+equal+quick_sort(large)
import random


def quick_sort(low, high, array):

    if low >= high:
        return

    index = random.randrange(low, high+1)
    pivot = array[index]
    array[index], array[high] = array[high], array[index]
    less = low
    large = high-1

    while less <= large:
        # 左边比pivot大，就交换到右边，右边此时已经比pivot大，large -1
        if array[less] > pivot:
            array[less], array[large] = array[large], array[less]
            large -= 1
            continue
        if array[large] < pivot:
            array[less], array[large] = array[large], array[less]
            less += 1
            continue

        # less <= pivot <= large满足，大家都进一步
        less += 1
        large -= 1

    # 当less - large = 1 时，跳出循环，此时所有的点都比较完毕，无论何种情况less所指都是一个大于等于pivot的元素，所以可以交换二者
    array[less], array[high] = array[high], array[less]
    # 这样array就被less所指的pivot分为了大于等于以及小于等于两边，可以继续挑出值比较了
    quick_sort(low, less-1, array)
    quick_sort(less+1, high, array)
    # return array
array = [0,21,3]
quick_sort(0,2,array)
print(array)