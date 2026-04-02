class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # maps course --> array of prereqs
        prereqs = defaultdict(list)

        # build directed graph
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        # from example: 0 --> 1

        def dfs(course):
            # cycle detected; cannot be taken
            if course in visited:
                return False

            # has no prerequisites; can be taken
            if prereqs[course] == []:
                return True

            visited.add(course)

            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            # optimisation - prevent repeated computations
            prereqs[course] = []
            return True
            
        # outer loop - check if all courses can be taken
        for course in range(numCourses):
            visited = set()
            if not dfs(course):
                return False

        # all courses can be taken
        return True