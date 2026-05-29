class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = defaultdict(list)

        # tree is technically "directed"
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        # cycle detection algorithm
        visited = set()

        def dfs(node, parent):
            # cycle detected
            if node in visited:
                return False

            visited.add(node)

            for nei in connections[node]:
                if nei == parent:
                    continue

                # cycle detected
                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        # must be fully connected
        return len(visited) == n