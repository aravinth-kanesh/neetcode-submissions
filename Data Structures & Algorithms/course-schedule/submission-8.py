class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)

        # to take course a, course b must be taken
        # build adjacency list of course -> [prereqs]
        for a, b in prerequisites:
            prereqs[a].append(b)

        print(prereqs.items())

        # track courses visited on current path
        visited = set()

        def dfs(course):
            # no prereqs
            if prereqs[course] == []:
                return True

            if course in visited:
                return False

            # add course to current path
            visited.add(course)

            for pre in prereqs[course]:
                # check if all prereqs can be taken
                if not dfs(pre):
                    return False

            # remove from current path
            visited.remove(course)

            # optimisation for when same course is visited on a diff
            # path
            prereqs[course] = []

            # course can be taken
            return True

        # main outer loop
        # loop through all courses and check if all can be taken
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True