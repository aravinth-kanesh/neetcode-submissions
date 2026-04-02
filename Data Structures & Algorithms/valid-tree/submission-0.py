class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = defaultdict(list)

        # build adj list
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        visited = set()

        def dfs(node, parent):
            # cycle detected
            if node in visited:
                return False

            visited.add(node)

            for neighbour in connections[node]:
                # undirected edges: parent should not considered as
                # part of cycle path
                if neighbour == parent:
                    continue

                # run dfs in neighbours
                # if any cycle is detected: not a valid tree
                if not dfs(neighbour, node):
                    return False

            # path is a valid tree
            return True

        # all reachable nodes from root are a valid tree if goes past this
        if not dfs(0, -1):
            return False

        # if all nodes aren't reachable, graph is not connected -> not a
        # valid tree
        return len(visited) == n