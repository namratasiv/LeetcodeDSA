class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        d = {}
        
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        maxele = max(d.values())    
        for ele in d:
            if maxele == d[ele] and d[ele] > (len(d)//2):
                return ele