from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # edge case - no grid
        if not grid:
            return -1

        minutes = fresh = 0
        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                # fresh fruit
                if grid[r][c] == 1:
                    fresh += 1
                # rotten fruit
                if grid[r][c] == 2:
                    # since multi-source bfs
                    queue.append((r, c))

        # now the queue has all of the initial rotten fruit
        # run bfs level-by-level, incrementing minutes for each level
        while queue and fresh:
            minutes += 1
            # process in level-order
            for _ in range(len(queue)):
                row, column = queue.popleft()

                # check all neighbours
                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc

                    # find neighbouring fresh fruits
                    if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] == 1:
                        # turn it rotten
                        grid[new_row][new_column] = 2
                        # decrement fresh
                        fresh -= 1
                        queue.append((new_row, new_column))

        # grid is invalid if all fresh fruit cannot become rotten
        return minutes if not fresh else -1