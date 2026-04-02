class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, columns = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < columns and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visited)

        # PACIFIC
        for c in range(columns):
            dfs(0, c, pacific)
        for r in range(1, rows):
            dfs(r, 0, pacific)

        # ATLANTIC
        for c in range(columns):
            dfs(rows - 1, c, atlantic)
        for r in range(rows - 1):
            dfs(r, columns - 1, atlantic)

        return list(pacific & atlantic)