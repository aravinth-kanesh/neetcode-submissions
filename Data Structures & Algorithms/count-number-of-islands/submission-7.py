class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs approach
        islands = 0

        if not grid:
            return islands 

        rows, columns = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # prevent duplicates from being visited - improves complexity
        visited = set()

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                row, column = stack.pop()

                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))

        # main loop
        # loop through every square - if it is a 1, mark as visited
        # and explore the entire island using bfs
        # count the number of islands
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    islands += 1
                    dfs(r, c)

        return islands
