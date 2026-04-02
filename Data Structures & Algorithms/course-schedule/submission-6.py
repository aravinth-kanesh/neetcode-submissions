class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # building an adjacency list
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        # store the courses on the current path
        visited = set()

        # returns True if a course can be taken, False otherwise
        # cycle detection algorithm
        # any cycle means the course cannot be taken
        def dfs(course):
            # cycle detected
            if course in visited:  
                return False

            # no prerequisites, then can be taken
            if prereqs[course] == []:
                return True

            visited.add(course)

            # loop through all prerequisites
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            # course can be taken
            
            # remove the course from the current path
            visited.remove(course)

            # optimisation - mark it as having no prereqs to simplify
            # time complexity if it ends up on the path of any other
            # courses
            prereqs[course] = []
            return True

        # all courses need to be able to be taken
        for course in range(numCourses):
            if not dfs(course):
                return False

        # all courses can be taken
        return True

