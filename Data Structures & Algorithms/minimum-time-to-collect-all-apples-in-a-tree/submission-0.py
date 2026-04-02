class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            total_time = 0

            for neighbour in connections[node]:
                if neighbour not in visited:
                    child_time = dfs(neighbour)

                    if child_time > 0 or hasApple[neighbour]:
                        total_time += child_time + 2

            return total_time

        return dfs(0)
