class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        rows, columns = len(grid), len(grid[0])

        queue = deque()

        def bfs(r, c):
            area = 1
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, column = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        area += 1
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            return area

        for r in range(rows):
            for c in range(columns):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area
