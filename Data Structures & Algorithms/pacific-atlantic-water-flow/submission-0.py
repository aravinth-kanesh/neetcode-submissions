class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # edge case
        if not heights:
            return []
        
        rows, columns = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 4 directions

        # all cells reachable from pacific and atlantic oceans respectively
        pacific, atlantic = set(), set()

        # reverse the logic - do dfs from edges and find all reachable
        # (in the "reverse" way) cells. Intersection of the two sets is
        # the answer
        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # reversed logic - can move to neighbours at a higher
                # level
                if 0 <= nr < rows and 0 <= nc < columns and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visited)
        
        # PACIFIC
        # left column
        for r in range(rows):
            dfs(r, 0, pacific)
        # top row
        for c in range(1, columns):
            dfs(0, c, pacific)

        # ATLANTIC
        # right column
        for r in range(rows):
            dfs(r, columns - 1, atlantic)
        # bottom row
        for c in range(columns - 1):
            dfs(rows - 1, c, atlantic)

        return list(pacific & atlantic)
