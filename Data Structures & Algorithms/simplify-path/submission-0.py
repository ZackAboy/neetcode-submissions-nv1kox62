class Solution:
    def simplifyPath(self, path: str) -> str:
        instructions = path.split("/")
        stack = []
        for i in instructions:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        if not stack:
            return "/"
        res = ""
        for s in stack:
            res = res + "/" + s

        return res