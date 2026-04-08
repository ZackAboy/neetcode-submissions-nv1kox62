class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        n = len(nums)
        prefix = []
        for i in nums:
            val = prev * i
            prefix.append(val)
            prev = val

        postfix = [0]*n
        prev = 1
        for i in range(n-1, -1, -1):
            val = prev * nums[i]
            postfix[i] = val
            prev = val

        print(prefix)
        print(postfix)

        res = []
        for i in range(n):
            prev = prefix[i-1] if i-1>=0 else 1
            nex = postfix[i+1] if i+1 <n else 1

            res.append(prev*nex)

        return res