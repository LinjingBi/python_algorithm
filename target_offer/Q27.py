'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._pre = None
        self.head = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.Convert(pRootOfTree.left)
        self._connect(pRootOfTree)
        self.Convert(pRootOfTree.right)
        return self.head

    def _connect(self, node):
        if self._pre:
            self._pre.right = node
        else:
            self.head = node
        node.left, self._pre = self._pre, node


pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)
pNode8 = TreeNode(8)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
# pNode5.right = pNode8

s = Solution()
p = s.Convert(pNode1)
while p:
    print(p.val)
    p = p.right
