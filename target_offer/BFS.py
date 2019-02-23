"""
深度优先搜索
"""
"""
用于没有权重的图，找一个节点到另一个节点的最短路径
"""

def BFS(g, s):
    res = {}
    if g and s:
        level = [s]
        while level:
            u = level.pop()
            # next_level = []
            for e in g.get_edges(u):
                v = e.opposite(u)
                if v not in res:
                    res[v] = e
                    level.append(v)
    return res







