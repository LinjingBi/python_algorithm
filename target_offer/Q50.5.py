'''
查找二叉搜索树两个结点的最低公共祖先
'''

"""
二叉搜索树的节点按中序遍历是一个从小到大排列的数组
左孩子 < 父节点 < 右孩子
那么最低公共祖先一定是最后一个大小位于两个节点之间的父节点
A的祖先/后代 包括A
不包括A的祖先/后代 叫真祖先/真后代
"""
INCORRECT_INPUT = False


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def lowestCommonAncestor(self, root, A, B):
        if not root or not A or not B:
            return INCORRECT_INPUT
        if A and B:
            while root:
                if (root.val - A.val) * (root.val - B.val) <= 0:
                    return root
                elif root.val < A.val and root.val < B.val:
                    root = root.right
                else:
                    root = root.left
        return False
