class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_colour = image[sr][sc]

        if original_colour == color:
            return image

        rows, columns = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([(sr, sc)])
        image[sr][sc] = color

        while queue:
            row, column = queue.popleft()

            for dr, dc in directions:
                new_row, new_column = row + dr, column + dc

                if 0 <= new_row < rows and 0 <= new_column < columns and image[new_row][new_column] == original_colour:
                    image[new_row][new_column] = color
                    queue.append((new_row, new_column))

        return image