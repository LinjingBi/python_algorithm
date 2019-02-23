'''
二叉树的右视图，利用层次遍历，先遍历右子树，每层的第一个放入结果数组
'''

'''
利用层次遍历，先将右孩子放入数组，这样每层数组的第一个就是右视图看到的节点
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_side_view(root):
    if root is None:
        return []
    level = [root]
    res = []
    while level:
        next_level = []
        for node in level:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        if next_level:
            res.append(next_level[0].val)
        level = next_level
    return res
