class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_max = nums[0]
        maxx=nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            curr_max = max(nums[i],nums[i]+curr_max)
            maxx = max(maxx,curr_max)
            
        return max(curr_max,maxx)