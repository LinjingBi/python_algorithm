'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

'''
由于有*存在
如果后一位是*，当前所对位数相等时（真实相等，或者有. ），就有三种情况
s+1，pattern+0   类似于 aaa，a*
s, pattern+2    类似于 ab   c*ab
s+1， pattern+2  类似于 ab  a*b
当我们判断完当前位的后一位为*的情况后，再判断正常情况（后一位不为*，当前位相等或者有.)
s+1 pattern+1
!!!所有的条件都要注意先判断s！=’‘,因为后文都要提取s[0]，如果为空字符，会报错！！！
在python中，任何大于字符串/数组/元祖 长度的切片，返回都是’‘/[]/()，空字符串/数组/元祖，不会报错。但如果是按下标访问，超限会报错

'''


class Solution:
    def match(self, s, pattern):
        if s is None or pattern is None:
            return False
        return self.matchcore(s, pattern)

    def matchcore(self, s, pattern):
        if not pattern:
            return False
        if s == pattern:
            return True

        if len(pattern) > 1 and pattern[1] == '*':
            # 注意先判断s不为空
            if s != '' and (pattern[0] == '.' or s[0] == pattern[0]):
                       # aaa a*aa                              aa  a*                           ab a*b
                return self.matchcore(s, pattern[2:]) or self.matchcore(s[1:], pattern) or self.matchcore(s[1:], pattern[2:])
            else:
                return self.matchcore(s, pattern[2:])

        if s != '' and (pattern[0] == '.' or s[0] == pattern[0]):
            return self.matchcore(s[1:], pattern[1:])

        return False


so = Solution()
print(so.match('aaa', '.aa'))
