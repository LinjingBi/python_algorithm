"""
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        import collections
        # 因为普通的dict是无序的,无法最第二次遍历找出第一个只出现一次的
        # ordereddict是插入的顺序
        dic = collections.OrderedDict()
        for each in s:
            if each in dic:
                dic[each] += 1
            else:
                dic[each] = 1

        # 注意加上.itmes()
        for key, value in dic.items():
            if value == 1:
                return key
        return -1


s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))

