from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dls(self, src, target, max_depth):
        if src == target:
            return True
        if max_depth <= 0:
            return False
        
        for i in self.graph[src]:
            if self.dls(i, target, max_depth-1):
                return True
        return False

    def dfid(self, src, target, max_depth):
        for i in range(max_depth):
            if self.dls(src, target, i):
                return True
        return False

# Create a graph
#        0
#      /   \
#     1      2
#    / \    | \
#   3   4  5   6


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

for i in range(2):
    target = [5, 6]
    maxDepth = [3, 2]
    src = 0

    if g.dfid(src, target[i], maxDepth[i]) == True:
        print("Target "+str(target[i]) + " is reachable from source within max depth of "+str(maxDepth[i]))
    else:
        print( "Target "+str(target[i]) + " is NOT reachable from source within max depth of "+str(maxDepth[i]))