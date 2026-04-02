class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)

        for course, prereq in prerequisites:
            pre[course].append(prereq)

        visited = set()
        def dfs(course):
            if not pre[course]:
                return True

            if course in visited:
                return False

            visited.add(course)
            for prereq in pre[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            pre[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True