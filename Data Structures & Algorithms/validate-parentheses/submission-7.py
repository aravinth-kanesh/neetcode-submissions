class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[':']'}

        # stack
        stack = []

        for bracket in s:
            # opening bracket
            if bracket in brackets:
                stack.append(bracket)
            # closing bracket
            else:
                # stack may be empty or bracket on top may not match
                if not stack or bracket != brackets[stack.pop()]:
                    return False

        # all brackets must be matched at the end, so empty stack
        return not stack