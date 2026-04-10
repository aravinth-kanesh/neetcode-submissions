class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        row_count = [0] * rows
        column_count = [0] * columns

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    column_count[c] += 1

        servers = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    if row_count[r] > 1 or column_count[c] > 1:
                        servers += 1

        return servers

    