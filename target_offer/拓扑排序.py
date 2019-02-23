"""
有向图的拓扑排序可以用来判断一个图是否有环，
如果最后拓扑排序返回的图的节点数不等于图的节点数，就说明有环
"""

"""
对于拓扑排序，最重要的一点就是要找到，入度为0的节点，如果一个图一个入度为0的节点，他就一定有环。
"""


def topo_sort(g):
    '''

    :param g: 图对象
           g.vertexs(): 返回一个包含图全部节点的数组
           g.incomes(v): 返回节点v的入度
           g.get_edges(u): 返回包含u节点的所有出边的数组
           e.opposite(u): 返回边对象e的除u外的另一个节点
    :return:
    '''

    if g:
        incomes_dict = {}  # 节点入度字典
        ready = []  # 保存入度为0的节点
        topo = []  # 返回拓扑排序遍历的节点

        # 先找到图中入度为0的节点
        for u in g.vertexs():
            incomes_dict[u] = g.incomes(u)
            if incomes_dict[u] == 0:
                ready.append(u)

        # 从入度为0的节点出发，遍历到它所指向的节点时，
        # 所指向节点入度减一，如果此时该节点入读为0，加入ready
        while ready:
            u = ready.pop()
            topo.append(u)
            for e in g.get_edges(u):
                v = e.opposite(u)
                incomes_dict[v] -= 1
                if incomes_dict[v] == 0:
                    ready.append(v)

        # 如果是无环图，所有节点都应该在topo内
        return True if len(topo) == len(g.vertexs()) else False
    return False
