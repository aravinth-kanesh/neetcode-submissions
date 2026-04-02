class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"

        for t in tokens:
            if t in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '+':
                    res = op1 + op2
                elif t == '-':
                    res = op1 - op2
                elif t == '*':
                    res = op1 * op2
                else:
                    res = int(float(op1) / op2)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]