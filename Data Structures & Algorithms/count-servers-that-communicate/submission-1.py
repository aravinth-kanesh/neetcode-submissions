class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        row_count, column_count = [0] * rows, [0] * columns
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    column_count[c] += 1

        servers = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (row_count[r] > 1 or column_count[c] > 1):
                    servers += 1

        return servers