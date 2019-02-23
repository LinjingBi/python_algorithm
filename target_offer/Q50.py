# 二叉树的最低公共祖先

"""
可以从根节点开始遍历，用链表记录到两个节点的路径，然后变成找两个链表的公共节点
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def lowestCommonAncestor(self, root, A, B):
        result = None
        if root:
            if A is B:
                return A
            road_A = self.find_road(root, A)
            road_B = self.find_road(root, B)
            if road_A and road_B:
                short, long = (road_A, road_B) if len(
                    road_A) < len(road_B) else (road_B, road_A)
                for i in range(1, len(short)):
                    result = short[-i]
                    if short[-i - 1] is not long[-i - 1]:
                        break
        return result

    def find_road(self, root, target):
        if root is target:
            return [target]
        if root is None or target is None:
            return []
        r_list = self.find_road(root.right, target)
        l_list = self.find_road(root.left, target)
        if r_list:
            r_list.append(root.right)
            return r_list
        elif l_list:
            l_list.append(root.left)
            return l_list
        return []
