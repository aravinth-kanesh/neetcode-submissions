class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            # current asteroid is moving left and top of stack asteroid
            # is moving right (collision)
            while stack and ast < 0 and stack[-1] > 0:
                # top of stack is smaller than current asteroid
                # top of stack destroyed, current asteroid keeps going
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                # same size - both are destroyed, break out the while
                elif stack[-1] == -ast:
                    stack.pop()
                # break applies for elif and else case, where the top
                # of stack is larger and the current asteroid gets
                # destroyed - so break out the while
                break
            else:
                # this is reached when we don't break out of the while
                # loop, when the asteroid survives
                stack.append(ast)

        return stack

