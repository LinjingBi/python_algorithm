'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def GetNext(self, pNode):
        result = None
        if pNode:
            if pNode.right:
                result = pNode.right
                while result.left:
                    result = result.left

            # elif pNode.parent.left:
            #     if pNode.parent.left is pNode:
            #         result = pNode.parent
            #
            # elif pNode.parent.right:
            #     if pNode.parent.right is pNode:
            #         right_parent = pNode.parent
            #         while right_parent.parent and right_parent is right_parent.parent.right:
            #             right_parent = right_parent.parent
            #         result = right_parent.parent
            else:
                result = pNode
                while result.parent and result.parent.right is result:
                    result = result.parent
                result = result.parent
        return result
