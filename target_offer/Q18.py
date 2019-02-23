'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def HasSubtree(self, root, s_root):
        result = False
        if root and s_root:
            # 节点相等，可以进一步比较
            if root.val == s_root.val:
                result = self.CheckSubtree(root, s_root)
            # 父节点不等，换成左右子节点继续比较
            if not result:
                result = self.HasSubtree(root.right, s_root)
            if not result:
                result = self.HasSubtree(root.left, s_root)
        return result

    def CheckSubtree(self, root, s_root):
        # 子结构为空，True
        if not s_root:
            return True
        # 子结构不为空，但root为空，False
        if not root:
            return False
        # 二者都不为空，但值不相等，False
        if root.val != s_root.val:
            return False
        # 二者不为空，值也相等，继续比较
        return self.CheckSubtree(root.right, s_root.right) and self.CheckSubtree(root.left, s_root.left)


pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))




