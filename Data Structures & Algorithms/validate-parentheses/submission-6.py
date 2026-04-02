class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        stack = []
        brackets = {'[': ']', '{': '}', '(': ')'}

        for bracket in s:
            # opening bracket
            if bracket in brackets:
                stack.append(bracket)
            else:
                # invalid parentheses
                if not stack or brackets[stack.pop()] != bracket:
                    return False

        return not stack