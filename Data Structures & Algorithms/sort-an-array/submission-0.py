class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(list):
            if len(list) <=1:
                return list

            mid = len(list)//2
            lh = list[:mid]
            rh = list[mid:]

            sortedl = mergesort(lh)
            sortedr = mergesort(rh)

            return merge(sortedl, sortedr)
        
        def merge(l, r):
            sort = []

            i = 0
            j = 0

            while i < len(l) and j < len(r):
                if l[i]<= r[j]:
                    sort.append(l[i])
                    i+=1
                else:
                    sort.append(r[j])
                    j+=1
            
            while i < len(l):
                sort.append(l[i])
                i+=1

            while j < len(r):
                sort.append(r[j])
                j+=1
            
            return sort

        return mergesort(nums)