'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def zhiprint(self, pHead):
        result = []
        if pHead:
            nodes = [pHead]
            event = 0
            while nodes:
                temp = []
                for node in nodes:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                result.append([nodes[(-1) * event + pow(-1, event) * i].val
                               for i in range(len(nodes))])
                event = not event
                nodes = temp
        return result

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

s = Solution()
print(s.zhiprint(pNode1))
