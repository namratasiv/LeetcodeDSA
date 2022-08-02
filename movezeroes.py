class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for x in range(count):
            nums.remove(0)
        for x in range(count):
            nums.append(0)
        