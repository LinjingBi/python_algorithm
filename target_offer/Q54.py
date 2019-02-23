class Solution:
    def isNumeric2(self, s):
        try:
            float(s)
            return True
            # if s[0:2] != '-+' and s[0:2] != '+-':
            #     return True
            # else:
            #     return False
        except ValueError:
            return False

s = Solution()
print(s.isNumeric2('12e5'))