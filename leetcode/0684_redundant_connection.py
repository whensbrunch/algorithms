class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.rank = [1] * (n + 1)

    def find(self, x):
        curr = x
        while curr != self.parents[curr]:
            self.parents[curr] = self.parents[self.parents[curr]]
            curr = self.parents[curr]
        return curr

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 0
        
        if self.rank[px] >= self.rank[py]:
            self.parents[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parents[px] = py
            self.rank[py] += self.rank[px]
        
        return 1

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(n for edge in edges for n in edge)
        uf = UnionFind(n)

        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge

        