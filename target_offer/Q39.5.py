"""
判断平衡二叉树
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def IsBalanced(self, Root):
        _, flag = self.balance_test(Root)
        return flag

    def balance_test(self, pRoot):
        if pRoot is None or (pRoot.right is None and pRoot.left is None):
            return 0, True
        l_h, l_flag = self.balance_test(pRoot.left)
        r_h, r_flag = self.balance_test(pRoot.right)
        # 注意这里，两个子树有一个不平衡，这棵树就不平衡，就不用算高度差，
        # 因为一颗子树不平衡，有可能他跟另一颗子树高度差满足平衡，如果只计算高度差
        # 就会忽略这种情况
        flag = False if not (
            l_flag and r_flag) else True if abs(
            l_h - r_h) < 2 else False
        # 还是要返回高度的，不要写成高度差了
        return 1 + max(l_h, r_h), flag


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode4.right = pNode5

S = Solution()
print(S.IsBalanced(pNode1))
