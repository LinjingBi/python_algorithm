'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''


class Solution:
    def Permutation(self, ss):
        if len(ss) < 2:
            return list(ss)
        array = list(ss)
        # 由于会有重复的元素，用sort将他们放在前后脚，好判断
        array.sort()
        group = []
        for index, val in enumerate(array):
            # 如果当下的元素和下一个元素相等，跳过当下元素
            if index != 0 and val == array[index-1]:
                continue
            # 注意permutation的入参是str类型，这里也要保持类型一致，虽然python无所谓。
            curr = self.Permutation(ss[:index] if index == len(array)-1 else ss[:index] + ss[index+1:])
            # 注意返回题目要求的返回类型是['ad','da']，这里用for正好把返回数组里的str遍历出来，然后合成
            for i in curr:
                group.append(val+i)
        return group

    # 扩展习题, 生成字符的所有组合
    # 比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], ab和ba属于不同的排列, 但属于同一个组合
    def group(self, ss):
        if len(ss) < 2:
            return list(ss)
        array = list(ss)
        # 虽然不是排列，但如果有重复元素也需要提早发现，减少递归次数
        array.sort()
        result = []
        for i in range(len(array)):
            # 只能放弃后一个，因为是递归i+1，如果放弃第一个重复的就会有损失，例如aabc，如果不考虑第一个a，那么结果就会缺少aa..的组合
            if i > 0 and array[i-1] == array[i]:
                continue
            # 同样保持入参为str类型
            curr = self.group(''.join(array[i+1:]))    # .join(str/[''])里面是可迭代的str类型，如果是list里面的元素必须全是str，不能是int
            # 算上自己
            result.append(array[i])
            for each in curr:
                result.append(array[i]+each)
            # 去重
            result = list(set(result))
            # 按字母顺序返回
            result.sort()
        return result


ss = 'abc'
S = Solution()
print(S.Permutation(ss))
print(S.group(ss))
