class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        from collections import Counter
        a = Counter(nums)
        final = []
        for x in a:
            
            if a[x] >1:
                final.append(x)
                
        return final
       