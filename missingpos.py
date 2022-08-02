class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        temp =  [x for x in range(1,len(nums)+2)]
        
        final = list(set(temp).difference(set(nums)))
        final = sorted(final)
        return final[0]
            
            