class Solution:
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        temp = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in temp:
                return [i,temp[diff]]
            temp[j] = i