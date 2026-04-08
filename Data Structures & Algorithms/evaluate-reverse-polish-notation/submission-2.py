import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif i == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif i == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif i == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                if (a / b) > 0:
                    stack.append(math.floor(a / b))
                else:
                    stack.append(math.ceil(a /  b))
            else:
                stack.append(i)
        return int(stack[-1])