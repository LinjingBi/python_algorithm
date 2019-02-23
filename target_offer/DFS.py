"""
深度优先搜索，利用递归
"""
"""
用于检查从一个节点到另一个节点是否有路径
"""

def DFS(g):
    """

    :param g: 图对象
           g.vertexs(): 返回图g的全部节点
    :return:
    """

    forest = {}
    if g:
        for u in g.vertexs():
            if u not in forest:
                DFS_core(g, u, forest)
    return forest


def DFS_core(g, s, discovered):
    for e in g.get_edges(s):
        v = e.opposite(s)
        if v not in discovered:
            discovered[v] = e
            DFS_core(g, v, discovered)





