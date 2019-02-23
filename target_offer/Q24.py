'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''


class Solution:
    def VerifySequenceOfBST(self, sequence):

        if not sequence:
            return False

        # 不需要单独把 1 列出来 为因1 跳过了所有的循环和比较，两个flag都是初值True，最终返回True
        # if len(sequence) == 1:
        #     return True

        # 后序遍历， 最后一个都是root
        root = sequence[-1]
        # 不要用range的i，单独计数
        left = 0
        # 分辨出左子树，左子树应该都比root小，同理可得右子树全部比root大
        for each in sequence[:-1]:
            if each > root:
                break
            left += 1
        # index大于等于left的都应该大于root，因为属于右子树，一旦不满足，就说明不是BST
        for each in sequence[left + 1:-1]:
            if each < root:
                return False
        # 递归判断左右子树
        # 针对len为2的情况如果0号元素小于-1号，left为1，这里进入左子树的递归，满足BST特性
        # 如果0号元素大于-1号，这里left为0，进入右子树的递归，满足BST特性
        # 给l_child,r_child设初值，是为了没有左子树或没有右子树或只有一个节点，能正常判断
        l_child = True
        # 有左子树
        if left > 0:
            l_child = self.VerifySequenceOfBST(sequence[:left])

        r_child = True
        # 有右子树
        if left < len(sequence) - 1:
            r_child = self.VerifySequenceOfBST(sequence[left:-1])

        return l_child and r_child


array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySequenceOfBST(array))
print(S.VerifySequenceOfBST(array2))
print(S.VerifySequenceOfBST(array3))