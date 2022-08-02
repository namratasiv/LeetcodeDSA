class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningsum = nums[0]
        final = [runningsum]
        for i in range(1,len(nums)):
            runningsum += nums[i]
            final.append(runningsum)
        return final