class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recur(curr, copen, cclose):
            if copen+cclose == 2*n:
                res.append("".join(curr))
                return
            
            if copen < n:
                curr.append("(")
                recur(curr, copen+1, cclose)
                curr.pop()

            if cclose <copen:
                curr.append(")")
                recur(curr, copen, cclose+1)
                curr.pop()

        recur([], 0, 0)

        return res