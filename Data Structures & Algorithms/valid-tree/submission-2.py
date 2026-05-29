class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        visited = set()

        def dfs(node, parent):
            # cycle detected
            if node in visited:
                return False

            visited.add(node)

            for nei in connections[node]:
                # ignore parent connections (not a cycle)
                if nei == parent:
                    continue

                # parent of nei is current node
                if not dfs(nei, node): 
                    return False

            # no cycles detected
            return True

        if not dfs(0, -1):
            return False

        # may not be fully connected
        return len(visited) == n