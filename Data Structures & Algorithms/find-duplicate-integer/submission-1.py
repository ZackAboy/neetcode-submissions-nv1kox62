class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        rep = 0

        while rep != slow:
            slow = nums[slow]
            rep = nums[rep]

        return rep