class Solution:
    def isValid(self, s: str) -> bool:
        brac = { "]":"[", ")":"(", "}":"{"}

        stack = []

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack and brac[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack

