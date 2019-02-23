'''
给定一颗二叉搜索树，请找出其中的第k小的结点。例如，
    5
   / \
  3  7
 /\ /\
2 4 6 8 中，
按结点数值大小顺序第三个结点的值为4。
'''
'''
二叉搜索树的第k个结点
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def kthnode(self, root, k):
        if k < 1 or not root:
            return None

        return self._inorder(k, root)

    # 中序遍历，迭代版
    def _inorder(self, k, root):
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            visit = stack.pop()
            if len(res) == k - 1:
                return visit.val
            res.append(visit.val)
            node = visit.right
        return None

    # 下面补充二叉树的后序遍历，递归版
    def _postorder(self, root):
        res = []
        if root:
            stack = []
            node = root
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                # 注意不是pop因为是后序遍历，父节点是最后遍历的，这里还要考察一下
                temp = stack[-1]
                # temp.right.val != res[-1]防止回溯过程，也就是此时的temp来自它右孩子的回溯，
                # 那么此时res[-1]就是上一轮才visit的temp.right
                # 此时对于temp父节点来说，它的左右孩子都已经visit了，
                # 所以一旦发现temp的right刚被遍历完，temp就失去了继续深入右子树的权利，
                # 而只能往上回溯（进入else）
                # 如果我们发现temp的右孩子，没有被visit，
                # 就代表此时到temp是用于深入还未开发的右子树，那么我们就执行if的内容
                if temp.right and temp.right.val != res[-1]:
                    node = temp.right
                # node为None，表示父节点已经被便利，此时是回溯过程，
                # 下一轮也是stack里的东西，不再需要遍历left，不然会变成死循环
                else:
                    stack.pop()
                    res.append(temp.val)  # 不要忘记放入的是val，不是节点
                    node = None
        return res

    # 前序遍历，迭代版
    def _preorder(self, root):
        res = []
        if root:
            stack = []
            node = root
            while node or stack:
                while node:
                    res.append(node.val)
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                node = node.right
        return res



# 测试后序遍历_postorder
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
pNode5.right = pNode8

s = Solution()
print(s._preorder(pNode1))
