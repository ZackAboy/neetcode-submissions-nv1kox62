class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recur(curr, copen, cclose):
            if copen+cclose == 2*n:
                res.append(curr)
                return
            
            if copen < n:
                recur(curr + "(", copen+1, cclose)

            if cclose <copen:
                recur(curr + ")", copen, cclose+1)

        recur("", 0, 0)

        return res