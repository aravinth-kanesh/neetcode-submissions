class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()

        # bfs function to explore the entire island and mark it as visited,
        # and return the size of the island
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            area = 0

            while queue:
                row, column = queue.popleft()
                area += 1

                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc

                    if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] == 1 and (new_row, new_column) not in visited:
                        visited.add((new_row, new_column))
                        queue.append((new_row, new_column))

            return area

        # outer loop
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    max_area = max(max_area, area)

        return max_area