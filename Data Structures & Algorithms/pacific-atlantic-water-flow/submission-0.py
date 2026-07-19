class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        pacificVisited = set()
        atlanticVisited = set()

        def dfs(i, j, visited):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]):
                return

            if (i, j) in visited:
                return

            visited.add((i, j))

            for dr, dc in directions:
                next_i = i + dr
                next_j = j + dc

                if (0 <= next_i < len(heights)
                    and 0 <= next_j < len(heights[0])
                    and heights[next_i][next_j] >= heights[i][j]):
                    dfs(next_i, next_j, visited)


        for i in range(len(heights)):
            dfs(i, 0, pacificVisited)
            dfs(i, len(heights[0]) - 1, atlanticVisited)

        for i in range(len(heights[0])):
            dfs(0, i, pacificVisited)
            dfs(len(heights) - 1, i, atlanticVisited)

        res = []
        for pos in pacificVisited:
            if pos in atlanticVisited:
                res.append(pos)
        
        return res


