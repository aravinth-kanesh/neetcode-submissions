class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'[': ']', '{': '}', '(': ')'}
        st = []

        for paren in s:
            # is an opening bracket
            if paren in parens:
                st.append(paren)
            # is a closing bracket
            else:
                # top gets popped regardless
                if not st or parens[st.pop()] != paren:
                    return False

        # could be the case that all closing brackets matched opening
        # ones, but there are still other brackets on the stack
        return not st