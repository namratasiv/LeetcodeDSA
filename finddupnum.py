class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        from collections import Counter
        d = Counter(nums)
        for x,y in d.items():
            
            if y> 1:
                return x
            