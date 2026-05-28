class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # instead of iterating through every square and seeing if water can
        # flow from it to both oceans, simulate water flow from both oceans
        # and find the intersection of both sets 
        rows, columns = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()

        def bfs(r, c, visited):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < columns and heights[nr][nc] >= heights[row][col] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        # main loop

        # pacific
        for c in range(columns):
            bfs(0, c, pacific)
        for r in range(1, rows):
            bfs(r, 0, pacific)

        # atlantic
        for c in range(columns):
            bfs(rows - 1, c, atlantic)
        for r in range(rows - 1):
            bfs(r, columns - 1, atlantic)

        # find intersection of sets
        return list(pacific & atlantic)

