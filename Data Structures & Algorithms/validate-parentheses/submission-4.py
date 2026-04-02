class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for bracket in s:
            # it's an opening bracket
            if bracket in brackets:
                stack.append(bracket)
            # it's a closing bracket
            else:
                if not stack or brackets[stack.pop()] != bracket:
                    return False

        # in the example case of "(("
        return not stack
