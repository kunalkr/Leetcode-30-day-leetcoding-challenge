from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1:]:
            res ^= num
        return res
        # return reduce(lambda x, y: x^y, nums, 0)
