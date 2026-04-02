class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        connections = defaultdict(list)

        # loop through every square
        for r in range(n):
            for c in range(n):
                # skip connections to itself
                if isConnected[r][c] == 1 and r != c:
                    connections[r].append(c)
                    connections[c].append(r)

        visited = set()

        def bfs(city):
            queue = deque([city])
            visited.add(city)

            while queue:
                c = queue.popleft()

                for neighbour in connections[c]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

        provinces = 0

        for city in range(n):
            if city not in visited:
                bfs(city)
                provinces += 1

        return provinces
