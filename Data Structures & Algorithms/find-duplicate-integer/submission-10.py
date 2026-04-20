class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        dupe = 0

        while dupe != slow:
            dupe = nums[dupe]
            slow = nums[slow]

        return slow