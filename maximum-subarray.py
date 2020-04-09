class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -2147483648
        temp_sum = 0
        
        for num in nums:
            temp_sum += num
            max_sum = max(max_sum, temp_sum)
            temp_sum = max(temp_sum, 0)
        return max_sum
