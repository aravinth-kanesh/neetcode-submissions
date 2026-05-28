class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)

        for course, prereq in prerequisites:
            pre[course].append(prereq)

        visiting = set()
        visited = set()
        res = []

        def dfs(course):
            # cycle detected
            if course in visiting:
                return False

            # already in res
            if course in visited:
                return True

            visiting.add(course)

            for prereq in pre[course]:
                # cycle detected
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res