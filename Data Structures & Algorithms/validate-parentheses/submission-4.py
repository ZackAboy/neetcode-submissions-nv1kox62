class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in range(len(s)):
            if s[x] == '(' or s[x] =="[" or s[x] == '{':
                stack.append(s[x])
            elif not stack:
                return False
            elif s[x] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[x] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[x] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

        if stack == []:
            return True
        else:
            return False
