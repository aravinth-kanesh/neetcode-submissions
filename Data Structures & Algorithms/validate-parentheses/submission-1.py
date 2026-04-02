class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for paren in s:
            if paren in parens:
                stack.append(paren)
            else:
                if not stack or parens[stack.pop()] != paren:
                    return False
        
        return not stack