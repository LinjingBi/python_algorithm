'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, root, sum):
        if not root:
            return []
        if root.right is None and root.left is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.FindPath(root.right, sum-root.val) + self.FindPath(root.left, sum-root.val)
        # 不能用i.append(root.val)，虽然i是一个数组，但是.append()没有返回值，不能成为[]的元素
        return [i + [root.val]for i in a]


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))
# 测试用例：[1,-2,-3,1,3,-2,null,-1]  -1
# 测试用例：[-2, None, -3] -5