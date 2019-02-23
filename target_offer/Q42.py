"""
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和普通字母一样处理
"""

class Solution:
    def ReverseSentence(self, s):
        temp = s.split(" ")
        return ' '.join(temp[::-1])  # 倒序输出[::-1]


st = 'I am a student.'
S = Solution()
print(S.ReverseSentence(st))
