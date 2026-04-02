class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        visited = set()

        def bfs(node):
            queue = deque([node])
            visited.add(node)

            while queue:
                cur = queue.popleft()
                for neighbour in connections[cur]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

        ccs = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                ccs += 1
        
        return ccs