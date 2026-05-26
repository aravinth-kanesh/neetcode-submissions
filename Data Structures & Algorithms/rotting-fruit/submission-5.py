class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source BFS problem: start BFS from all rotten fruit
        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()

        # count number of fresh fruit and add all rotten fruit to queue
        fresh = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0)) # (row, column, time)

        # edge case - all rotten already
        if fresh == 0:
            return 0

        print(f"Fresh fruit left: {fresh}")

        # queue now has (r, c) pairs of all initial rotten fruit
        # simulation stops when no fresh fruit left
        while queue and fresh:
            r, c, time = queue.popleft()
            print(f"Row: {r}, Column: {c} popped at time {time}!")

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                    fresh -= 1
                    print(f"Row: {nr}, Column: {nc} turned rotten!")
                    print(f"Fresh fruit left: {fresh}")

                    if fresh == 0:
                        return time + 1

                    grid[nr][nc] = 2 # turn it rotten
                    queue.append((nr, nc, time + 1))

        return -1