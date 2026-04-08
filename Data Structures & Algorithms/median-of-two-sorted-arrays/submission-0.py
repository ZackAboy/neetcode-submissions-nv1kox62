class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        t = len(nums1)+ len(nums2)
        mid = (t + 1)//2
        l = 0
        r = len(nums1)

        while l <= r:
            i = (l + r)//2
            j = mid - i

            if i>0:
                l1 = nums1[i-1]
            else:
                l1 = float('-inf')
            if i < len(nums1):
                r1 = nums1[i]
            else:
                r1 = float('inf')
            if j > 0:
                l2 = nums2[j-1]
            else:
                l2 = float('-inf')
            if j < len(nums2):
                r2 = nums2[j]
            else:
                r2 = float('inf')

            if l2<=r1 and l1<=r2:
                if t%2 == 1:
                    return float(max(l1, l2))
                else:
                    return float((max(l1, l2) + min(r1, r2))/2)

            elif l1>r2:
                r = i-1
            else:
                l = i+1