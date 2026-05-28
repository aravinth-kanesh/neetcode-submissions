class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list (course -> prereqs)
        prereqs = defaultdict(list)

        for a, b in prerequisites:
            prereqs[a].append(b)

        # all courses on current path
        visited = set()
        
        # cycle detected - course cannot be taken
        def dfs(course):
            # cycle detected
            if course in visited:
                return False

            # no prereqs - can be taken
            if not prereqs[course]:
                return True

            # add the course to the current path
            visited.add(course)

            for prereq in prereqs[course]:
                # cycle detected
                if not dfs(prereq):
                    return False

            visited.remove(course)
            prereqs[course] = [] # optimisation
            return True

        # main loop
        for course in range(numCourses):
            # course cannot be taken
            if not dfs(course):
                return False

        # all courses can be taken
        return True