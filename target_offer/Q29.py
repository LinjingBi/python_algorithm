'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# 如果出现的次数超过一半，那么该数字的总次数-其他元素的次数之和将大于0


class Solution:
    def MoreThanHalfNum(self, numbers):
        if len(numbers) == 0:
            return
        count = 0
        chosen_one = numbers[0]

        for integer in numbers:
            if chosen_one == integer:
                count += 1
            else:
                if count > 1:
                    count -= 1
                else:
                    chosen_one = integer
                    count = 1
        times = 0
        for each in numbers:
            if each == chosen_one:
                times += 1
        return chosen_one if times > len(numbers) / 2 else None


S = Solution()
print(S.MoreThanHalfNum([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum([1, 2]))
