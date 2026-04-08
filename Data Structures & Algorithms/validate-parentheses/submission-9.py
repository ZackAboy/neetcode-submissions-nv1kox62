class Solution:
    def isValid(self, s: str) -> bool:
        brac = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if stack and brac[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack