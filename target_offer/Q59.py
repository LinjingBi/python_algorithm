'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


"""
思考镜像后的树，看以root的左右子树，左子树的左孩子镜像后变为右子树的右孩子，
左子树的右孩子镜像后变成右子树的左孩子，依次类推，就有了递归的表达式。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        return self._comparecore(pRoot, pRoot)

    def _comparecore(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        elif pRoot1 is None or pRoot2 is None:
            return False
        elif pRoot2.val != pRoot1.val:
            return False
        return self._comparecore(pRoot1.right, pRoot2.left) and self._comparecore(pRoot1.left, pRoot2.right)

    # def isSymmetrical2(self, pRoot):
    #     result = False
    #     if pRoot:
    #         import collections
    #         dq = collections.deque([pRoot])
    #         while dq:
    #             node = dq.popleft()
    #             if node.right is None and node.left is None:
    #                 result = True
    #                 break
    #             elif node.right is None or node.left is None:
    #                 result = False
    #                 break
    #             else:
    #                 if node.right.val == node.left.val:
    #                     dq.extend([node.left, node.right])
    #                     continue
    #                 result = False
    #                 break
    #     return result






pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(6)
pNode4 = TreeNode(5)
pNode5 = TreeNode(9)
pNode6 = TreeNode(9)
pNode7 = TreeNode(5)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
r = S.isSymmetrical(pNode1)
print(r)
