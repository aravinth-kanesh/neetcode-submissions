class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pacific, atlantic = set(), set()

        def dfs(row, column, visited):
            stack = [(row, column)]

            while stack:
                row, column = stack.pop()

                if (row, column) in visited:
                    continue

                visited.add((row, column))

                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc

                    if 0 <= new_row < rows and 0 <= new_column < columns and heights[new_row][new_column] >= heights[row][column]:
                        stack.append((new_row, new_column))

        for c in range(columns):
            dfs(0, c, pacific)
        for r in range(1, rows):
            dfs(r, 0, pacific)

        for c in range(columns):
            dfs(rows - 1, c, atlantic)
        for r in range(rows - 1):
            dfs(r, columns - 1, atlantic)

        return list(pacific & atlantic)