class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        edges = []
        for i in range(N):
            for j in range(N):
                if isConnected[i][j] == 1:
                    edges.append([i, j])
        
        parents = [i for i in range(N)]
        rank = [1] * N

        def find(n):
            curr = n
            while curr != parents[curr]:
                # path compression
                parents[curr] = parents[parents[curr]]
                curr = parents[curr]
            return curr
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            combined_rank = rank[p1] + rank[p2]
            if rank[p1] >= rank[p2]:
                parents[p1] = p2
            else:
                parents[p2] = p1
            rank[p1] = combined_rank
            rank[p2] = combined_rank

            return 1
        
        res = N
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res

        
        