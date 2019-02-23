'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

'''
在python3里，
对于.sort(), sorted()等有key比较参数的BIF来说，key只能接受用于单个元素的比较函数（比较函数只有一个入参），
而在python2里，以上的BIF还有一个cmp入参，可以设置用于有两个入参的比较函数，py3没有，
所以我们就用functools.cmp_to_key，将一个cmp函数打包成key。cmp(x, y)，这样x的用于排序的key就是cmp的结果
'''

'''
采用的方法是冒泡法， 一位一位的确定，从第0位开始，冒泡比较，如果组成的y+x大于x+y就交换位置，
这样就保证了，x这个位置上的整数跟x以后的任何一个元素组合带来的都是x这一位上的最小值。
'''


class Solution:
    # 用sorted来简化冒泡法的代码
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''

        from functools import cmp_to_key

        key = cmp_to_key(lambda x, y: int(
            str(x) + str(y)) - int(str(y) + str(x)))
        numbers.sort(key=key)
        # 只是介绍一下cmp_to_key的用法，这里的返回类型不是str，但顺序一致
        return numbers
    # 冒泡法

    def PrintMinNumber2(self, num):
        # 考虑为None，后面len会报错，为[]倒无所谓，不过也一起包含了
        if not num:
            return ''
        str_num = [str(each) for each in num]
        for i in range(len(str_num)):
            for j in range(i + 1, len(str_num)):
                if str_num[i] + str_num[j] > str_num[j] + str_num[i]:
                    str_num[i], str_num[j] = str_num[j], str_num[i]
        # 如果str_num为[],join不会报错，返回''，
        # 但是只要不为空，数组里面就必须是str类型的元素，因为join是str的BIF
        return ''.join(str_num)


numb = [3, 32, 321]
s = Solution()
print(s.PrintMinNumber2(numb))
