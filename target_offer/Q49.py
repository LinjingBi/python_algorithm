'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数
'''

"""
整数还包括正负整数，如果时有符号的整数第一位就是+/- 剩余的就该全是数字，如果不是就是违规输入
"""
INCORRECT = 0


class Solution:
    def StrToInt(self, s):
        if s:
            if s.startswith('+') or s.startswith('-'):
                try:
                    result = self.trans_to_int(s[1:])
                    return result if not result or s.startswith(
                        '+')else -1 * result
                except IndexError:
                    return INCORRECT
            else:
                return self.trans_to_int(s)
        return INCORRECT

    def trans_to_int(self, s):
        nums = 0
        # 由于python里两个str没有减法操作，所以不能用c++的i-’0‘
        chart = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9}
        for i in s:
            if i in chart:
                # 每次nums扩大十倍，加在个位上
                nums = nums * 10 + chart[i]
            else:
                return INCORRECT
        return nums
test = '-12356'
s = Solution()
print(s.StrToInt(test))