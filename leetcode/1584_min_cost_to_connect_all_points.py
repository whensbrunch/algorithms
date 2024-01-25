class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        N = len(points)
        edges = []
        for i in range(N):
            for j in range(i+1, N):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, distance))
        edges = sorted(edges, key=lambda x: x[2])

        mst_size = 0
        mst_cost = 0
        uf = UnionFind(N)
        for x, y, cost in edges:
            if uf.union(x, y):
                mst_size += 1
                mst_cost += cost
            
            if mst_size == N - 1:
                break
        
        return mst_cost
            
        