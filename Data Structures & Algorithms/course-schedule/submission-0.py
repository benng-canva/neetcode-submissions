class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if len(graph[crs]) == 0:
                return True

            visited.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            graph[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
    def buildGraph(self, n, edges):
        graph = [set() for i in range(n)]
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
        
        return graph
            