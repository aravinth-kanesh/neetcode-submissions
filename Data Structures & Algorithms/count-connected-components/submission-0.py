class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = 0
        visited = set()
        connections = defaultdict(list)

        # create adjacency list 
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        # strategy: loop through all nodes, explore all connected nodes
        # , count ccs
        def bfs(node):
            queue = deque([node])
            visited.add(node)

            while queue:
                cur = queue.popleft()

                for neighbour in connections[cur]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

        for i in range(n):
            if i not in visited:
                bfs(i)
                cc += 1

        return cc