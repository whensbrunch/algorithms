class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [1] * (n+1)

    def find(self, x: int):
        curr = x
        while curr != self.par[curr]:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] <= self.rank[py]:
            self.par[px] = py
            self.rank[py] += self.rank[px]
        else:
            self.par[py] = px
            self.rank[px] += self.rank[py]
        return True



class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        edges = sorted(connections, key=lambda x: x[2])
        mst_cost = 0
        mst_size = 0
        uf = UnionFind(n)
        for x, y, cost in edges:
            merged = uf.union(x, y)
            if merged:
                mst_cost += cost
                mst_size += 1
        

        return -1 if mst_size != n - 1 else mst_cost

        