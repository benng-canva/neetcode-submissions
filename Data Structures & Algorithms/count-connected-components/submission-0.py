class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        for vertex in range(n):
            if vertex in visited:
                continue

            count += 1
            dfs(vertex)

        return count