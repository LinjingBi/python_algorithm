'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # 递归实现
    def Mirror(self, root):
        if not root:
            return None
        root.right, root.left = root.left, root.right

        self.Mirror(root.right)
        self.Mirror(root.left)
    # def Mirror(self, root):
    #     if root is None:
    #         return
    #     if root.left is None and root.right is None:
    #         return root
    #     pTemp = root.left
    #     root.left = root.right
    #     root.right = pTemp
    #
    #     self.Mirror(root.left)
    #     self.Mirror(root.right)

    # 迭代实现，层次遍历，deque是一个双向队列，可以实现队列(append,popleft)和栈(append,pop)的功能

    def Mirror2(self, root):
        if not root:
            return
        import collections
        dq = collections.deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            # if node:
            #     dq.extend([node.left, node.right])
            #     node.right, node.left = node.left, node.right
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

            node.right, node.left = node.left, node.right


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()

S.Mirror2(pNode1)
print(pNode1.right.left.val)





