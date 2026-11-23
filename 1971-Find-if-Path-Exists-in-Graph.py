from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)   # undirected, so add the reverse edge too
        visited = {source}
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return False