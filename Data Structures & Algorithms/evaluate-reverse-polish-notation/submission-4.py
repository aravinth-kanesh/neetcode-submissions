class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-/*"

        for token in tokens:
            if token in ops:
                op2, op1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                if token == '/':
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(token))

        return stack[0]