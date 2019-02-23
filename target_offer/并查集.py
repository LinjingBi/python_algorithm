'''
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
'''


class Solution:

    def __init__(self):
        self._cluster = None

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        self._cluster = [i for i in range(len(M))]

        result = len(M)

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    # 一旦发现两个人是好友，就找他们的parent，不一样的话就join
                    i_parent = self._find(i)
                    j_parent = self._find(j)
                    if i_parent != j_parent:
                        # 注意是改j_parent不是j，join只涉及parent层次的改变。
                        self._cluster[j_parent] = i_parent
                        result -= 1
        return result

    # 这里把find拿出来写了，也可以放在findCircleNum里当个闭包。
    def _find(self, i):
        # 因为每次两个组合join的时候，都只是改了组合parent的parent，组合内部的元素都能没有改
        # 所以只要发现i不等于cluster[i]就说明它不是parent，那么它最新的parent可能已经在join中被改
        # 所以要递归找最新的parent，然后返回
        if self._cluster[i] != i:
            self._cluster[i] = self._find(self._cluster[i])
        return self._cluster[i]

