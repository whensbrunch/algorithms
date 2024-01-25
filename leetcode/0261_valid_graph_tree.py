from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Approach: check that graph is connected and acyclic
        # by starting a dfs or bfs from any node

        # look for opportunities to short circuit
        if n != len(edges) + 1: # checking number of edges and nodes
            return False
        
        if not n:
            return True
        
        # create the adjency list from the list of edges
        adj = defaultdict(list)
        for start, end in edges:        
            adj[start].append(end)
            adj[end].append(start)

        def dfs(node, prev, visited) -> bool:
            # if node was already visited, we have a cycle
            if node in visited:
                return False
            else:
                visited.add(node)

            # visit all neighbors
            for neighbor in adj[node]:
                # ...except for the one we just came from
                if neighbor == prev:
                    continue
                
                # short-circuit if we detect a cycle
                if not dfs(neighbor, node, visited):
                    return False

            return True
        
        visited = set()
        acyclic = dfs(0, -1, visited)
        return acyclic and len(visited) == n
