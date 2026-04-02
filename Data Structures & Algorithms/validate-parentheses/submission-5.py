class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        brackets = {'{': '}', '[': ']', '(': ')'}
        stack = []

        for bracket in s:
            # is an opening bracket
            if bracket in brackets:
                # push to stack
                stack.append(bracket)
            # is a closing bracket
            else:
                # non-matching brackets
                # empty stack means invalid string
                if not stack or brackets[stack.pop()] != bracket:
                    return False

        # stack must be empty for the string to be valid
        return not stack