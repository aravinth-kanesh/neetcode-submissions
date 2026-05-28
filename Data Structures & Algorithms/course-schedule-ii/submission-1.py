class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)

        for a, b in prerequisites:
            prereqs[a].append(b)

        visiting = set()
        visited = set()
        order = []

        def dfs(course):
            # cycle detected
            if course in visiting:
                return False

            # already done
            if course in visited:
                return True

            visiting.add(course)

            for pre in prereqs[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course) # remove from current path
            visited.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order

            