class UndirtectedGraphNode:
    def __init__(self, x):
        # 节点的符号
        self.label = x
        # 指向的其他节点的数组，如果有指向自己，自己也在里面
        self.neighbors = []


class Solution:
    def clone_graph(self, firstnode):
        if firstnode is None or firstnode.neighbors == '[]':
            return UndirtectedGraphNode(firstnode.label) if firstnode else None

        visited = {}
        self._DFS(firstnode.neighbors, UndirtectedGraphNode(firstnode.label), visited)
        return visited[firstnode.label]

    def _DFS(self, neighbors, nex, visited):
        # 因为只有不在visited里的才会递归，所以不用条件判断，直接放入visited
        visited[nex.label] = nex
        for each in neighbors:
            # 注意neighbors里面存的是node类，而visited的key是node.label
            if each.label in visited:
                node = visited[each.label]
            else:
                node = UndirtectedGraphNode(each.label)
                self._DFS(each.neighbors, node, visited)
            nex.neighbors.append(node)
        return




