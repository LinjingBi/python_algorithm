'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''

class Solution:
    # def NumberOf1Between1AndN_Solution(self, n):
        # time = n//10
        # if n%10 > 0:
        #     time += 1
        # return time
    def NumberOf1Between1AndN_Solution(self, n):
            ones, m = 0, 1
            while m <= n:
                #       计算第m位之高位有多少个1，如果n//m小于2 +8也不会改变取整结果
                ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
                #                                 是否第m位为1          为1 表示低m位 只有低m位字面大小+1个1  不为1 这一部分就乘0，低m位的可能性就归在+8上
                m *= 10

            return ones

    def NumberOf1Between1AndN2(self, n):
        ones, m = 0, 1
        while m <= n:
            if ((n // m) % 10) != 0 and ((n // m) % 10) != 1:
                ones += (n // 10 // m + 1) * m
            elif ((n // m) % 10) == 1:
                ones += (n // m // 10) * m + n % m + 1

            m *= 10

        return ones

s = Solution()
print(s.NumberOf1Between1AndN_Solution(100))
print(s.NumberOf1Between1AndN2(10))
