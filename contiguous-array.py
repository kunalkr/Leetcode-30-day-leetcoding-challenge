class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        curr_sum = 0
        sum_hash = {0:0}
        
        # nums = [num if num == 1 else -1 for num in nums]
        
        for i, num in enumerate(nums):
            curr_sum += 2*num - 1
            
            # if curr_sum == 0:
            #     max_len = i + 1
            
            if curr_sum in sum_hash:
                max_len = max(max_len, i - sum_hash[curr_sum] + 1)
            else:
                sum_hash[curr_sum] = i + 1
        
        return max_len
