'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

"""
一组数字，全部异或，如果都是成对出现，结果为0
如果有一个只出现一次，结果为该数
这道题，有两个不同，我们就要把数组分成两组，每组一个不同，然后全部异或
就找出了不同的两个数
数组可以全部异或一遍，结果就是不同两个数异或的结果，只要找出结果二进制形式为1的一位，说明这一位两数不同
然后以此位为界，把全部的数组分为两组，一样的数一定会在一组，再分开异或，各自结果就是不同的两个数
"""
"""
python中 异或^ 二进制右移>>
0和任何数异或都是该数
"""
class Solution:
    def FindNumsAppearOnce(self, array):
        if not array or len(array) < 2:
            return
        i = 0
        # i是两个不同的数异或的结果
        for each in array:
            i ^= each
        print(i)
        # 找i第一个1，也就是两个数二进制形式下第一个不同的位数
        sep = self.find_sep(i)

        # 按照第sep位是1，把数组分为两组，各有一个不同的数
        # 千万不能写成group1=group2=[]，这样都指向一个底层数组，两个数组就一摸一样了
        group1 = []
        group2 = []
        for each in array:
            num = each >> sep
            if num % 2 == 0:
                group1.append(each)
            else:
                group2.append(each)

        # find_diff将两组数分别异或，各找一个不同
        diff1 = self.find_diff(group1)
        diff2 = self.find_diff(group2)

        return diff1, diff2

    def find_sep(self, i):
        count = 0
        # >>每次移位都不是原地的，所以要再次赋值给i
        # 如果第一位是1，肯定是奇数
        while i % 2 == 0:
            i >>= 1
            count += 1
        return count

    def find_diff(self, group):
        diff = 0
        for each in group:
            diff ^= each
        return diff




aList = [2, 4, 3, 6, 3, 2, 5, 5]
s = Solution()
print(s.FindNumsAppearOnce(aList))

