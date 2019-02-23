'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

'''
需要两个数组配合，先是数组A先放入root，然后数组B放置遍历root的right，left，遍历完root后
数组A被放入result，然后更新数组A为数组B，数组B清零，然后重新遍历数组A，放置入数组B。依次循环，直到数组A为空
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def LevelOrder(self, pRoot):
        res = []
        if pRoot:
            nodes = [pRoot]
            while nodes:
                temp = []
                # 层次遍历
                for node in nodes:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                res.append([node.val for node in nodes])
                nodes = temp
        return res


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
print(s.LevelOrder(pNode1))
# [[8], [6, 10], [5, 7, 9, 11]]
