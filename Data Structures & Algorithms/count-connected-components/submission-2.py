class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        visited = set()

        def dfs(node):
            stack = [node]
            visited.add(node)

            while stack:
                cur = stack.pop()
                for neighbour in connections[cur]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append(neighbour)

        ccs = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ccs += 1
        
        return ccs