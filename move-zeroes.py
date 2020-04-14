class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[k] = num
                k += 1
        for i in range(len(nums) - k):
            nums[k + i] = 0
