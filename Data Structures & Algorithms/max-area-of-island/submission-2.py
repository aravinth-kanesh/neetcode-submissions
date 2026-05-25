class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def bfs(r, c):
            area = 0
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, column = queue.popleft()
                print(f"Popped: Row = {row}, Column = {column}")
                area += 1

                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            # island fully explored, return island area
            print(f"Area: {area}")
            return area

        # main loop
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area