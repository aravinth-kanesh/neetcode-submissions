class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # track visited nodes
        # use dfs to fully explore a cc
        # number of dfs calls made is the number of ccs
        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in connections[node]:
                if nei not in visited:
                    dfs(nei)

        ccs = 0

        # main loop
        for node in range(n):
            if node not in visited:
                dfs(node)
                ccs += 1

        return ccs
