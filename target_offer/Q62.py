'''
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''
"""
序列化是指把二叉树按前序遍历的顺序变成字符串输出
节点之间用，隔开，如果节点的左孩子或者右孩子为空，值为#（还要加上，隔开）
反序列化是指根据序列化的字符串，恢复一颗二叉树
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def serialize(self, root):
        res = ''
        if root:
            stack = []
            # 如果root不为None就有可能在往stack里加东西
            # 如果stack不为空，就会再pop出新的root
            while root or stack:
                # 先遍历父节点，然后是左孩子，如果左孩子不存在，跳出
                while root:
                    stack.append(root)
                    res += str(root.val) + ','
                    root = root.left
                # 左孩子不在，添加#
                res += '#,'
                # 找当前节点的右孩子
                root = stack.pop()
                root = root.right
        # 最后一个叶子节点因为没有左孩子，就会加上‘#,’
        # 由于是最后一个节点，不需要加','，所以要去掉最后一位
        # 如果root为None，返回#
        return res[:-1] if res else '#'

    def deserialize(self, ser):
        root, _ = self._de_core(ser, sp=0)
        return root

    # 利用递归完成复原，创建顺序也是先父节点->左孩子->右孩子
    def _de_core(self, ser, sp):
        # 一旦有#出现表示，左孩子为空，需要开始安排右孩子
        if not ser or ser[sp] == '#':
            return None, sp + 1
        # 依照前序遍历的规律，第一个就是根节点，然后根节点的左孩子。。。。
        node = TreeNode(int(ser[sp]))
        # 记得+1，指向下一个字符
        sp += 1
        # 利用前序遍历的规则，第一个一定是root，然后依次往后找到最左的孩子，然后由于最左的孩子没有左孩子
        # 触碰递归基，返回None，同时sp+1，使得sp指向ser的下一个字符串，也就是最左的右孩子
        # 所以复原的顺序和前序遍历一致，从根节点开始创建，然后一路向左，到头，再换右，在一路向左
        node.left, sp = self._de_core(ser, sp)
        node.right, sp = self._de_core(ser, sp)
        return node, sp
