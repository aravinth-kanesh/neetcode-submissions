class Solution:
    def isValid(self, s: str) -> bool:
        match_brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        bracket_stack = []

        for bracket in s:
            if bracket in match_brackets:
                bracket_stack.append(bracket)
            elif bracket_stack and match_brackets[bracket_stack[-1]] == bracket:
                bracket_stack.pop()
            else:
                return False

        return len(bracket_stack) == 0
         
