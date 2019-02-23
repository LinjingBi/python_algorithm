'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 递归版，算高度，对于树来说，深度和高度大小一样，对于节点来说不一样
    def TreeDepth(self, pRoot):
        # 如果pRoot没有孩子节点，也就是是个叶子的时候就要返回，叶子节点高度为0
        if pRoot is None or (pRoot.right is None and pRoot.left is None):
            return 0

        return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))

    # 迭代版，类似于层次遍历，用队列
    # 利用层次遍历，每次左右孩子入栈都要带上父节点的深度
    # dp最后一个节点，一定是最深的叶子节点，直接返回它的深度
    def TreeDepth2(self, pRoot):
        count = 0
        import collections
        if pRoot:
            dp = collections.deque([(pRoot, count)])
            while dp:
                node, count = dp.popleft()
                if node.left:
                    dp.append((node.left, count + 1))
                if node.right:
                    dp.append((node.right, count + 1))
        return count


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
print(S.TreeDepth(None))
